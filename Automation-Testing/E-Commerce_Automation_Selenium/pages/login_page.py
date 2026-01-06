"""Login page object"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page locators and methods"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    
    def enter_username(self, username):
        """Enter username in the field"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password in the field"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Complete login process"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_displayed(self.ERROR_MESSAGE)