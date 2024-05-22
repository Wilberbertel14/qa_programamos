from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()

button = driver.find_element(By.LINK_TEXT, "REGISTER") .click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,700)")
time.sleep(3)

email = driver.find_element(By.XPATH, "//input[contains(@id,'email')]")
email.send_keys("wilber@gmail.com")
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
password.send_keys("123456")
time.sleep(2)

confirmPassword = driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]")
confirmPassword.send_keys("123456")
time.sleep(2)

button = driver.find_element(By.XPATH, "//input[@src='images/submit.gif']") .click()
#button.send_keys(Keys.ENTER)
time.sleep(5)



driver.close()

