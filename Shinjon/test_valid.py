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

# --- VALID INPUT TEST ---
try:
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys("Md Rahim Khan")

    driver.execute_script("document.getElementsByName('phone')[0].value='01712345678';")
    driver.execute_script("document.getElementsByName('emergency')[0].value='01812345678';")

    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.NAME, "address").send_keys("Dhaka 1212")

    driver.find_element(By.NAME, "health_issues").clear()
    driver.find_element(By.NAME, "health_issues").send_keys("Diabetes")

    driver.find_element(By.NAME, "nid").clear()
    driver.find_element(By.NAME, "nid").send_keys("1234567890123")

    driver.find_element(By.NAME, "update_patient_profile").click()
    time.sleep(2)

    print("Valid input test completed")

except Exception as e:
    print("Test failed:", e)

driver.quit()