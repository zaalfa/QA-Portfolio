"""Products page object"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class ProductsPage(BasePage):
    """Products page locators and methods"""
    
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def get_page_title(self):
        """Get page title text"""
        return self.get_text(self.PAGE_TITLE)
    
    def is_page_loaded(self):
        """Check if products page is loaded"""
        return self.get_page_title() == "Products"
    
    def get_product_count(self):
        """Get number of products displayed"""
        products = self.find_elements(self.INVENTORY_ITEMS)
        return len(products)
    
    def add_first_product_to_cart(self):
        """Add first product to cart"""
        # Wait for button to be clickable
        button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTONS)
        )
        button.click()
        # Wait for cart badge to update or appear
        time.sleep(0.5)
    
    def add_multiple_products(self, count):
        """Add multiple products to cart"""
        for i in range(count):
            # Get all ADD buttons (excluding REMOVE buttons)
            add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
            
            if add_buttons:
                # Click first available ADD button
                self.wait.until(EC.element_to_be_clickable(add_buttons[0]))
                add_buttons[0].click()
                # Wait for button to change to REMOVE
                time.sleep(0.3)
    
    def get_cart_item_count(self):
        """Get cart badge count"""
        try:
            # Wait a bit for badge to appear if items were just added
            time.sleep(0.2)
            badge = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return badge.text
        except:
            return "0"
    
    def click_cart(self):
        """Click cart icon"""
        self.click(self.CART_ICON)
        # Wait for cart page to load
        self.wait_for_url_contains("cart")
    
    def logout(self):
        """Logout from application"""
        # Click burger menu
        self.click(self.BURGER_MENU)
        
        # Wait for sidebar to appear
        logout_link = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.LOGOUT_LINK)
        )
        logout_link.click()
        
        # Wait for redirect to login page
        time.sleep(1)