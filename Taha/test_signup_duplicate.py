from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost/DocMate/DocMateV3/public/signup_doctor.php")
time.sleep(2)


driver.find_element(By.ID, "name").send_keys("Dr Test User")
driver.find_element(By.ID, "email").send_keys("doctest1@gmail.com")
driver.find_element(By.ID, "phone").send_keys("01712345678")


degrees = ["MBBS", "MD", "FCPS"]  # Add more if needed
for degree in degrees:
    driver.find_element(By.XPATH, f"//input[@value='{degree}']").click()


driver.find_element(By.ID, "bmdc").send_keys("BMDC12345")
driver.find_element(By.ID, "nid").send_keys("1234567890123")


driver.find_element(By.ID, "address").send_keys("Dhaka")
driver.find_element(By.ID, "chamber").send_keys("Dhanmondi")


days = ["Sun", "Mon"]
for day in days:
    driver.find_element(By.XPATH, f"//input[@value='{day}']").click()

# --- Time (trigger change event for JS) ---
driver.execute_script("""
let from = document.getElementById('time_from'); 
from.value='10:00'; 
from.dispatchEvent(new Event('change'));
let to = document.getElementById('time_to'); 
to.value='14:00'; 
to.dispatchEvent(new Event('change'));
""")


driver.find_element(By.ID, "desc").send_keys("Experienced in general medicine and specialized care.")


driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "confirm_password").send_keys("123456")

time.sleep(1)


driver.execute_script("document.getElementById('doctorSignupForm').submit()")

time.sleep(5) 

print("Current URL after submission:", driver.current_url)

driver.quit()