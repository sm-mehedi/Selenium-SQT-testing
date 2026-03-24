from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost/DocMate/DocMateV3/public/login.php")

time.sleep(2)

email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")

email.send_keys("test@gmail.com")
password.send_keys("123456")

password.send_keys(Keys.RETURN)

time.sleep(3)

print("After login URL:", driver.current_url)

driver.quit()