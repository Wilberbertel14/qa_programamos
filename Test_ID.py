from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

name = driver.find_element(By.ID, "userName")
name.send_keys("selenium")
time.sleep(2)

email = driver.find_element(By.ID, "userEmail")
email.send_keys("wilber@gmail.com")
time.sleep(2)

Current_Address = driver.find_element(By.ID, "currentAddress")
Current_Address.send_keys("Sincelejo")
time.sleep(2)

Permanent_Address =driver.find_element(By.ID, "permanentAddress")
Permanent_Address.send_keys("Sincelejo_city")
time.sleep(2)

#comando para hacer scroll
driver.execute_script("window.scrollTo(0,250)")
time.sleep(2)

button = driver.find_element(By.ID, "submit") .click()
#button.send_keys(Keys.ENTER)
time.sleep(2)

driver.close()