"""Login functionality tests"""

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import Config


@pytest.mark.login
class TestLogin:
    """Test cases for login functionality"""
    
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """Verify successful login with valid credentials"""
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        products_page = ProductsPage(driver)
        assert products_page.is_page_loaded(), "User should be redirected to Products page"
        assert "inventory.html" in driver.current_url, "URL should contain inventory"
    
    def test_invalid_username(self, driver):
        """Verify login fails with invalid username"""
        login_page = LoginPage(driver)
        login_page.login("invalid_user", Config.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text, "Should show mismatch error"
    
    def test_invalid_password(self, driver):
        """Verify login fails with invalid password"""
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, "wrong_password")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert "Username and password do not match" in login_page.get_error_message()
    
    def test_empty_username(self, driver):
        """Verify login fails with empty username"""
        login_page = LoginPage(driver)
        login_page.login("", Config.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert "Username is required" in login_page.get_error_message()
    
    def test_empty_password(self, driver):
        """Verify login fails with empty password"""
        login_page = LoginPage(driver)
        login_page.login(Config.VALID_USERNAME, "")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert "Password is required" in login_page.get_error_message()
    
    def test_both_fields_empty(self, driver):
        """Verify login fails with both fields empty"""
        login_page = LoginPage(driver)
        login_page.login("", "")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert "Username is required" in login_page.get_error_message()
    
    def test_locked_out_user(self, driver):
        """Verify locked out user cannot login"""
        login_page = LoginPage(driver)
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), "Should show locked out message"
    
    @pytest.mark.parametrize("username, password, expected_error", [
        ("", "", "Username is required"),
        ("valid_user", "", "Password is required"),
        ("", "valid_pass", "Username is required"),
        ("invalid", "invalid", "Username and password do not match"),
    ])
    def test_invalid_login_scenarios(self, driver, username, password, expected_error):
        """Data-driven test for invalid login scenarios"""
        login_page = LoginPage(driver)
        login_page.login(username, password)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        assert expected_error in login_page.get_error_message()


@pytest.mark.login
class TestLogout:
    """Test cases for logout functionality"""
    
    def test_successful_logout(self, logged_in_driver):
        """Verify user can logout successfully"""
        driver = logged_in_driver
        products_page = ProductsPage(driver)
        
        assert products_page.is_page_loaded(), "Should be on products page"
        
        products_page.logout()
        
        # Verify redirected to login page
        assert driver.current_url == Config.BASE_URL + "/", "Should redirect to login page"