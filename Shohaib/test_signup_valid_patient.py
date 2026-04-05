from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://localhost/DocMate/DocMateV3/public/signup_patient.php")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "patientSignupForm"))
    )
    
    driver.find_element(By.NAME, "name").send_keys("Test Patient")
    
    # Force valid Bangladeshi phone numbers
    driver.execute_script("document.getElementsByName('phone')[0].value = '01712345678';")
    driver.execute_script("document.getElementsByName('emergency')[0].value = '01812345678';")
    
    driver.find_element(By.NAME, "address").send_keys("Dhaka, Bangladesh")
    driver.find_element(By.NAME, "nid").send_keys("1234567890123")
    driver.find_element(By.NAME, "email").send_keys("patienttest1@gmail.com")
    
    health_issues = ["diabetes", "hypertension"]
    for issue in health_issues:
        checkbox = driver.find_element(By.XPATH, f"//input[@value='{issue}']")
        driver.execute_script("arguments[0].click();", checkbox)
    
    driver.find_element(By.NAME, "other_conditions").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.NAME, "confirm_password").send_keys("123456")
    
    time.sleep(1)
    driver.execute_script("document.getElementById('patientSignupForm').submit()")
    
    time.sleep(5)
    
    try:
        print("Current URL after submission:", driver.current_url)
    except:
        print("Could not get URL (session may have closed).")

finally:
    driver.quit()