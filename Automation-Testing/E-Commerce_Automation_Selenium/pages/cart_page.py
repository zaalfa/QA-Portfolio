"""Cart page object"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class CartPage(BasePage):
    """Cart page locators and methods"""
    
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    
    def get_cart_item_count(self):
        """Get number of items in cart"""
        # Don't wait if cart is empty
        time.sleep(0.3)  # Small delay for page to render
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def remove_first_item(self):
        """Remove first item from cart"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTONS)
        )
        button.click()
        time.sleep(0.5)  # Wait for item to be removed
    
    def remove_all_items(self):
        """Remove all items from cart"""
        while True:
            buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if not buttons:
                break
            buttons[0].click()
            time.sleep(0.3)
    
    def is_checkout_button_displayed(self):
        """Check if checkout button is displayed"""
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.CHECKOUT_BUTTON)
            )
            return button.is_displayed()
        except:
            return False
    
    def click_continue_shopping(self):
        """Click continue shopping button"""
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        )
        button.click()
        # Wait for products page to load
        self.wait_for_url_contains("inventory")