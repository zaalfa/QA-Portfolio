"""Products functionality tests"""

import pytest
from pages.products_page import ProductsPage
import time


@pytest.mark.products
class TestProducts:
    """Test cases for products page functionality"""
    
    @pytest.mark.smoke
    def test_products_page_loads(self, logged_in_driver):
        """Verify products page loads successfully"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        assert products_page.is_page_loaded(), "Products page should load"
        assert products_page.get_page_title() == "Products", "Page title should be 'Products'"
    
    def test_product_count(self, logged_in_driver):
        """Verify correct number of products displayed"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        product_count = products_page.get_product_count()
        assert product_count == 6, "Should display 6 products"
    
    def test_initial_cart_badge(self, logged_in_driver):
        """Verify cart badge is not displayed initially"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        cart_count = products_page.get_cart_item_count()
        assert cart_count == "0", "Cart should be empty initially"
    
    @pytest.mark.smoke
    def test_add_single_product(self, logged_in_driver):
        """Verify adding single product to cart"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_first_product_to_cart()
        time.sleep(1)  # Wait for cart badge to update
        cart_count = products_page.get_cart_item_count()
        
        assert cart_count == "1", "Cart should show 1 item"
    
    def test_add_multiple_products(self, logged_in_driver):
        """Verify adding multiple products to cart"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        items_to_add = 3
        products_page.add_multiple_products(items_to_add)
        time.sleep(1)  # Wait for cart badge to update
        cart_count = products_page.get_cart_item_count()
        
        assert cart_count == str(items_to_add), f"Cart should show {items_to_add} items"
    
    def test_add_all_products(self, logged_in_driver):
        """Verify adding all products to cart"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        total_products = products_page.get_product_count()
        products_page.add_multiple_products(total_products)
        time.sleep(1)  # Wait for cart badge to update
        cart_count = products_page.get_cart_item_count()
        
        assert cart_count == str(total_products), f"Cart should show all {total_products} items"
    
    def test_navigate_to_cart(self, logged_in_driver):
        """Verify navigation to cart page"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        products_page.add_first_product_to_cart()
        time.sleep(1)
        products_page.click_cart()
        
        assert "cart.html" in driver.current_url, "Should navigate to cart page"