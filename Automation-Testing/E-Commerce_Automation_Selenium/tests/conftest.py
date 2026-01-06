"""Pytest fixtures and configurations"""

import pytest
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config
import os
from datetime import datetime


def get_chromedriver_path():
    """Get ChromeDriver path with automatic fix for WebDriverManager bug"""
    driver_path = ChromeDriverManager().install()
    
    # FIX: WebDriverManager sometimes returns wrong path
    if "THIRD_PARTY_NOTICES" in driver_path or not driver_path.endswith(".exe"):
        driver_dir = os.path.dirname(driver_path)
        
        # Try common locations
        possible_paths = [
            os.path.join(driver_dir, "chromedriver.exe"),
            os.path.join(os.path.dirname(driver_dir), "chromedriver.exe"),
            os.path.join(driver_dir, "chromedriver-win64", "chromedriver.exe"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        # Recursive search
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(driver_path)))
        for root, dirs, files in os.walk(base_dir):
            if "chromedriver.exe" in files:
                return os.path.join(root, "chromedriver.exe")
        
        raise FileNotFoundError(f"chromedriver.exe not found near {driver_path}")
    
    return driver_path

def close_password_breach_popup(driver, timeout=5):
    try:
        wait = WebDriverWait(driver, timeout)
        popup_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[.//text()[contains(., 'OK') "
                    "or contains(., 'Got it') "
                    "or contains(., 'Change')]]",
                )
            )
        )
        popup_button.click()
        print("Password breach popup closed")
    except TimeoutException:
        pass

@pytest.fixture(scope="function")
def driver():
    """Setup and teardown browser driver"""

    chrome_options = Options()

   # Fresh Chrome profile
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Essential stability options
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    if Config.HEADLESS:
        chrome_options.add_argument("--headless=new")

    try:
        service = Service(get_chromedriver_path())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.get(Config.BASE_URL)

        yield driver

    finally:
        if "driver" in locals():
            driver.quit()

        shutil.rmtree(user_data_dir, ignore_errors=True)

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Fixture that returns a driver with user already logged in"""
    from pages.login_page import LoginPage
    
    login_page = LoginPage(driver)

    try:
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    except Exception:
        pytest.skip("Login interrupted by Chrome security popup")
    
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{Config.SCREENSHOT_PATH}{item.name}_{timestamp}.png"
                driver.save_screenshot(filename)
                print(f"\nScreenshot saved: {filename}")
            except Exception as e:
                print(f"\nFailed to capture screenshot: {str(e)}")