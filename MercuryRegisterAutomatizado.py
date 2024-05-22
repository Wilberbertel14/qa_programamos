from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/index.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

buttonRegister = driver.find_element(By.LINK_TEXT, "REGISTER") .click()
time.sleep(1)

try:
    registerImag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='images/mast_register.gif']"))
        )

    if registerImag:
        
        print("!Bienvenido a la página del registro¡")
        print("Por favor procede a llenar los campos")

    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)

    mail = driver.find_element(By.XPATH, "//input[contains(@id,'email')]") .send_keys("WB@gmail.com")
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]") .send_keys("Prueba.01")
    time.sleep(1)

    confirmPassword = driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]") .send_keys("Prueba.01")
    time.sleep(1)

    button = driver.find_element(By.XPATH, "//input[@src='images/submit.gif']") .click()
    time.sleep(2)

    confirmationMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Note: Your user name is WB@gmail.com.')]"))
        )

   
    if confirmationMessage:
        print("Mensaje de confirmación encontrado")
        print(confirmationMessage.text)
except Exception as e:
    print("Error al cargar la pagina de resgister", e)

finally:
    driver.close()