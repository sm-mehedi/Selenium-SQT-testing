from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost/DocMate/DocMateV3/public/signup_patient.php")
time.sleep(2)

# --- Test invalid inputs ---
driver.find_element(By.NAME, "name").send_keys("")  # Empty Name
driver.find_element(By.NAME, "phone").send_keys("12345")  # Invalid phone
driver.find_element(By.NAME, "emergency").send_keys("abcd")  # Invalid emergency
driver.find_element(By.NAME, "address").send_keys("123")  # Too short
driver.find_element(By.NAME, "nid").send_keys("abc")  # Invalid NID
driver.find_element(By.NAME, "email").send_keys("invalid-email")  # Invalid email
driver.find_element(By.NAME, "password").send_keys("123")  # Too short
driver.find_element(By.NAME, "confirm_password").send_keys("321")  # Not matching

# Select a couple of checkboxes (optional, valid)
health_checkboxes = ["diabetes", "asthma"]
for value in health_checkboxes:
    driver.find_element(By.XPATH, f"//input[@value='{value}']").click()

# Other conditions
driver.find_element(By.NAME, "other_conditions").send_keys("Testing other conditions input")

time.sleep(1)

# Submit form
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

# Check for error messages
error_fields = ["name", "phone", "emergency", "address", "nid", "email", "password", "confirm_password"]
for field in error_fields:
    try:
        error_text = driver.find_element(By.XPATH, f"//input[@name='{field}']/following-sibling::span").text
        print(f"{field} error: {error_text}")
    except:
        print(f"No visible error for {field}")

driver.quit()