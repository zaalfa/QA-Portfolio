# Saucedemo E-Commerce Test Automation 🐍

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15-green)
![Pytest](https://img.shields.io/badge/Pytest-7.4-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Overview
A comprehensive test automation framework for the **Saucedemo e-commerce application**
built using **Python**, **Selenium WebDriver**, and **Pytest**, following the
**Page Object Model (POM)** design pattern.

This project demonstrates real-world QA automation practices including
test organization, stability considerations, and clear documentation of known limitations.

## 🎯 Test Coverage

### ✅ Login Functionality (10 test cases)
- Valid login scenarios
- Invalid credentials handling
- Empty field validations
- Locked user scenarios
- Data-driven parametrized testing
- Logout functionality

### ✅ Products Management (7 test cases)
- Product listing validation
- Add single/multiple products
- Cart badge updates
- Navigation flows
- Product count verification

### ✅ Shopping Cart (7 test cases)
- Empty cart validation
- Add/remove items
- Cart persistence across navigation
- Checkout button presence
- Continue shopping functionality

**Core functional flows validated with documented browser-level limitations**

## 🏗️ Framework Architecture
```
📦 Project Structure
├── 📂 pages/              # Page Object classes
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page object
│   ├── products_page.py   # Products page object
│   └── cart_page.py       # Cart page object
├── 📂 tests/              # Test cases
│   ├── conftest.py        # Pytest fixtures & hooks
│   ├── test_login.py      # Login tests
│   ├── test_products.py   # Product tests
│   └── test_cart.py       # Cart tests
├── 📂 utils/              # Utilities
│   └── config.py          # Configuration settings
├── 📂 reports/            # Test reports (auto-generated)
├── 📂 screenshots/        # Failure screenshots (auto-generated)
├── requirements.txt       # Dependencies
├── pytest.ini            # Pytest configuration
└── README.md             # This file
```
### 🎨 Design Patterns & Best Practices
- **Page Object Model (POM)**: Separation of page elements and test logic
- **DRY Principle**: Reusable methods in BasePage
- **Explicit Waits**: Robust synchronization
- **Fixtures**: Setup/teardown automation
- **Parametrized Tests**: Data-driven testing
- **Hooks**: Screenshot capture on failure
- **Markers**: Test categorization (smoke, regression)

## 🛠️ Technologies & Tools

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Programming Language |
| Selenium WebDriver | 4.15.2 | Browser Automation |
| Pytest | 7.4.3 | Testing Framework |
| WebDriver Manager | 4.0.1 | Automatic driver management |
| Pytest-HTML | 4.1.1 | HTML reporting |

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Chrome browser (latest version)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/saucedemo-selenium-python.git
cd saucedemo-selenium-python
```

2. **Create virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running Tests

**Run all tests:**
```bash
pytest
```

**Run with HTML report:**
```bash
pytest --html=reports/report.html --self-contained-html
```

**Run specific test file:**
```bash
pytest tests/test_login.py
```

**Run specific test:**
```bash
pytest tests/test_login.py::TestLogin::test_valid_login
```

**Run smoke tests only:**
```bash
pytest -m smoke
```

**Run with specific markers:**
```bash
pytest -m login          # Run login tests
pytest -m products       # Run product tests
pytest -m cart           # Run cart tests
pytest -m "smoke or regression"  # Run smoke OR regression tests
```

**Run in parallel:**
```bash
pytest -n auto  # Auto-detect CPU cores
pytest -n 4     # Use 4 workers
```

**Run in headless mode:**
Edit `utils/config.py` and set `HEADLESS = True`, then run:
```bash
pytest
```

**Verbose output:**
```bash
pytest -v  # Verbose
pytest -vv # Extra verbose
```

## 📊 Test Reports

After test execution, reports are generated in:
- `reports/report.html` - HTML test report with pass/fail status
- `screenshots/` - Screenshots of failed tests (auto-captured)

**View HTML Report:**
```bash
# Windows
start reports/report.html

# Mac
open reports/report.html

# Linux
xdg-open reports/report.html
```

## 🔒 Known Limitation

During UI-based login automation, Google Chrome may display a browser-level security popup such as **"Password found in a data breach"**.

This popup:
- Is generated by the **Chrome browser**, not by the application under test
- Exists **outside the application DOM**
- Cannot be reliably detected, disabled, or dismissed using Selenium WebDriver
- May block user interaction and cause **login-related test cases to fail intermittently**

At the moment, no technical workaround is implemented in this framework to suppress or handle this popup.  
Affected test cases are intentionally left unchanged to reflect this real-world limitation.


## 🎨 Key Features

✨ **Page Object Model** - Maintainable and scalable structure  
✨ **Explicit Waits** - Robust element synchronization  
✨ **Auto Screenshots** - Capture failures automatically  
✨ **Parametrized Tests** - Data-driven testing support  
✨ **Parallel Execution** - Faster test runs  
✨ **Custom Fixtures** - Pre/post-logged-in states  
✨ **Test Markers** - Categorize and filter tests  
✨ **HTML Reports** - Beautiful test reports  
✨ **Auto Driver Management** - No manual driver setup  

## 📈 Test Execution

### Sample Output
```bash
========== test session starts ==========
platform win32 -- Python 3.10.0, pytest-7.4.3
plugins: html-
