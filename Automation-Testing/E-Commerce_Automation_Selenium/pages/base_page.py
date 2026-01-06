"""Base page class with common methods for all pages"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.config import Config


class BasePage:
    """Base page class that all page objects inherit from"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find multiple elements"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        """Click element with wait for clickable"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Send keys to element with wait for visibility"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def get_title(self):
        """Get page title"""
        return self.driver.title
    
    def wait_for_url_contains(self, url_part, timeout=10):
        """Wait for URL to contain specific text"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_contains(url_part))
    
    def get_element_count(self, locator):
        """Get count of elements without waiting (for empty lists)"""
        try:
            elements = self.driver.find_elements(*locator)
            return len(elements)
        except:
            return 0