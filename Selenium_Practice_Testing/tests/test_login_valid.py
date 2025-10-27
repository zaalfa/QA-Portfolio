from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Setup WebDriver
service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Pastikan folder screenshots ada
os.makedirs("screenshots", exist_ok=True)

try:
    # 1️⃣ Buka website utama
    driver.get("https://practicesoftwaretesting.com/")

    # 2️⃣ Klik tombol "Sign in"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-sign-in']"))
    )
    driver.find_element(By.CSS_SELECTOR, "a[data-test='nav-sign-in']").click()

    # 3️⃣ Isi email & password
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    driver.find_element(By.ID, "email").send_keys("zalfarmdhni@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Test01-123")

    # 4️⃣ Klik tombol login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-test='login-submit']"))
    )
    driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']").click()

    # 5️⃣ Verifikasi login berhasil dengan My Account
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1[data-test='page-title']"))
        )
        title_text = driver.find_element(By.CSS_SELECTOR, "h1[data-test='page-title']").text
        if "my account" in title_text.lower():
            print("✅ Login berhasil! Halaman:", title_text)
            driver.save_screenshot("screenshots/login_success.png")
        else:
            print("❌ Login gagal (halaman tidak sesuai).")
            driver.save_screenshot("screenshots/login_failed.png")
    except:
        print("❌ Login gagal (elemen My Account tidak ditemukan).")
        driver.save_screenshot("screenshots/login_failed.png")

except Exception as e:
    print("⚠️ Terjadi error:", e)
    driver.save_screenshot("screenshots/error.png")

finally:
    driver.quit()
