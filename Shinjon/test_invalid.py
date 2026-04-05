from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# --- LOGIN ---
driver.get("http://localhost/DocMate/DocMateV3/public/login.php")
time.sleep(2)

driver.find_element(By.NAME, "email").send_keys("rahim@gmail.com")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

# --- GO TO PROFILE ---
try:
    driver.find_element(By.LINK_TEXT, "My Profile").click()
except:
    print("Profile link not found")
    driver.quit()
    exit()

time.sleep(2)

# --- INVALID INPUT TEST ---
try:
    # Invalid name (empty)
    driver.find_element(By.NAME, "name").clear()

    # Invalid phone
    driver.execute_script("document.getElementsByName('phone')[0].value='01234567890';")

    # Invalid emergency
    driver.execute_script("document.getElementsByName('emergency')[0].value='00000000000';")

    # Invalid address (too short)
    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.NAME, "address").send_keys("Dh")

    # Invalid health issues (empty)
    driver.find_element(By.NAME, "health_issues").clear()

    # Invalid NID (too short)
    driver.find_element(By.NAME, "nid").clear()
    driver.find_element(By.NAME, "nid").send_keys("123")

    # Submit
    driver.find_element(By.NAME, "update_patient_profile").click()
    time.sleep(2)

    # Check error message (if exists)
    try:
        error = driver.find_element(By.CLASS_NAME, "error")
        print("Error shown:", error.text)
    except:
        print("No error message found (validation may be client-side)")

except Exception as e:
    print("Test failed:", e)

driver.quit()