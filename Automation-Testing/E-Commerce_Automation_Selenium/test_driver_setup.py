"""Test ChromeDriver setup with path fix"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_chromedriver():
    print("\n=== Testing ChromeDriver Setup ===")
    
    # Download driver
    print("Downloading ChromeDriver...")
    driver_path = ChromeDriverManager().install()
    print(f"Downloaded path: {driver_path}")
    
    # FIX: WebDriverManager returns wrong path
    # It points to THIRD_PARTY_NOTICES instead of chromedriver.exe
    if "THIRD_PARTY_NOTICES" in driver_path or not driver_path.endswith(".exe"):
        # Get directory
        driver_dir = os.path.dirname(driver_path)
        # Find chromedriver.exe in parent directories
        possible_paths = [
            os.path.join(driver_dir, "chromedriver.exe"),
            os.path.join(os.path.dirname(driver_dir), "chromedriver.exe"),
            os.path.join(os.path.dirname(os.path.dirname(driver_dir)), "chromedriver.exe"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                driver_path = path
                print(f"✓ Fixed path: {driver_path}")
                break
        else:
            # Search recursively
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(driver_path)))
            for root, dirs, files in os.walk(base_dir):
                if "chromedriver.exe" in files:
                    driver_path = os.path.join(root, "chromedriver.exe")
                    print(f"✓ Found chromedriver.exe at: {driver_path}")
                    break
    
    # Verify file exists
    if not os.path.exists(driver_path):
        print(f"✗ ERROR: chromedriver.exe not found!")
        return
    
    print(f"✓ Using driver: {driver_path}")
    
    # Initialize browser
    print("Initializing Chrome browser...")
    options = Options()
    options.add_argument("--headless=new")
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    # Test navigation
    print("Testing navigation...")
    driver.get("https://www.google.com")
    print(f"✓ Page title: {driver.title}")
    
    # Show versions
    print(f"✓ Chrome version: {driver.capabilities['browserVersion']}")
    print(f"✓ ChromeDriver version: {driver.capabilities['chrome']['chromedriverVersion'].split()[0]}")
    
    driver.quit()
    print("\n=== SUCCESS! ChromeDriver working properly! ===\n")

if __name__ == "__main__":
    test_chromedriver()