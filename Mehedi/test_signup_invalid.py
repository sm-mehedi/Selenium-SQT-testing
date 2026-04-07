from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost/DocMate/DocMateV3/public/signup_doctor.php")
time.sleep(2)

# --- INVALID INPUTS ---
driver.find_element(By.ID, "name").send_keys("")  
driver.find_element(By.ID, "email").send_keys("invalid-email")  
driver.find_element(By.ID, "phone").send_keys("123")  



driver.find_element(By.ID, "bmdc").send_keys("")  # Empty BMDC
driver.find_element(By.ID, "nid").send_keys("")   # Empty NID
driver.find_element(By.ID, "address").send_keys("")  # Empty address
driver.find_element(By.ID, "chamber").send_keys("")  # Empty chamber

# Time fields left empty to trigger JS validation
driver.execute_script("""
let from = document.getElementById('time_from'); 
from.value=''; 
from.dispatchEvent(new Event('change'));
let to = document.getElementById('time_to'); 
to.value=''; 
to.dispatchEvent(new Event('change'));
""")

driver.find_element(By.ID, "desc").send_keys("")


driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "confirm_password").send_keys("654321")  

time.sleep(1)



time.sleep(3)

# Capture validation errors
errors = driver.find_elements(By.CLASS_NAME, "validation-error")
for i, error in enumerate(errors, start=1):
    if error.is_displayed():
        print(f"Error {i}: {error.text}")

driver.quit()