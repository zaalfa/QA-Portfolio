"""Configuration settings for the test framework"""

class Config:
    # Base URL
    BASE_URL = "https://www.saucedemo.com"
    
    # Browser settings
    BROWSER = "chrome"  # chrome, firefox, edge
    HEADLESS = False
    IMPLICIT_WAIT = 15  # Increased from 10
    EXPLICIT_WAIT = 15  # Increased from 10
    
    # Test users
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    LOCKED_USERNAME = "locked_out_user"
    
    # Paths
    SCREENSHOT_PATH = "screenshots/"
    REPORT_PATH = "reports/"