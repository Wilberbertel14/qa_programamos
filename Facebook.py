from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time 

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

elemento=driver.find_element(By.NAME, "q")
elemento.send_keys("facebook")
elemento.send_keys(Keys.RETURN)
time.sleep(2)

wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Facebook - Inicia sesión o regístrate')]"))).click()

driver.quit()
