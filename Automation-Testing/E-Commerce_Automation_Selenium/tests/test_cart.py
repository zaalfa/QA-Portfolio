"""Shopping cart functionality tests"""

import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import time


@pytest.mark.cart
class TestCart:
    """Test cases for shopping cart functionality"""
    
    def test_empty_cart(self, logged_in_driver):
        """Verify empty cart displays no items"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.click_cart()
        cart_page = CartPage(driver)
        
        item_count = cart_page.get_cart_item_count()
        assert item_count == 0, "Empty cart should show 0 items"
    
    @pytest.mark.smoke
    def test_cart_with_items(self, logged_in_driver):
        """Verify cart displays added items correctly"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_multiple_products(2)
        time.sleep(1)  # Wait for cart to update
        products_page.click_cart()
        
        cart_page = CartPage(driver)
        item_count = cart_page.get_cart_item_count()
        
        assert item_count == 2, "Cart should display 2 items"
    
    def test_remove_single_item(self, logged_in_driver):
        """Verify removing item from cart"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_multiple_products(3)
        time.sleep(1)
        products_page.click_cart()
        
        cart_page = CartPage(driver)
        initial_count = cart_page.get_cart_item_count()
        
        cart_page.remove_first_item()
        time.sleep(0.5)
        updated_count = cart_page.get_cart_item_count()
        
        assert updated_count == initial_count - 1, "Cart should have one less item"
    
    def test_remove_all_items(self, logged_in_driver):
        """Verify removing all items from cart"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_multiple_products(3)
        time.sleep(1)
        products_page.click_cart()
        
        cart_page = CartPage(driver)
        cart_page.remove_all_items()
        
        time.sleep(0.5)
        final_count = cart_page.get_cart_item_count()
        
        assert final_count == 0, "Cart should be empty after removing all items"
    
    def test_checkout_button_displayed(self, logged_in_driver):
        """Verify checkout button is displayed"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_first_product_to_cart()
        time.sleep(1)
        products_page.click_cart()
        
        cart_page = CartPage(driver)
        assert cart_page.is_checkout_button_displayed(), "Checkout button should be visible"
    
    def test_continue_shopping(self, logged_in_driver):
        """Verify continue shopping button works"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_first_product_to_cart()
        time.sleep(1)
        products_page.click_cart()
        
        cart_page = CartPage(driver)
        cart_page.click_continue_shopping()
        
        assert "inventory.html" in driver.current_url, "Should return to products page"
    
    def test_cart_persistence(self, logged_in_driver):
        """Verify cart persists items across page navigation"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_multiple_products(2)
        time.sleep(1)  # Wait for cart to update
        initial_count = products_page.get_cart_item_count()
        
        products_page.click_cart()
        time.sleep(0.5)
        driver.back()
        time.sleep(0.5)  # Wait for page to load
        
        persisted_count = products_page.get_cart_item_count()
        assert persisted_count == initial_count, "Cart should maintain item count"