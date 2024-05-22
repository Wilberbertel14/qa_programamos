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

buttonRegister = driver.find_element(By.LINK_TEXT, "SIGN-ON") .click()
time.sleep(2)
 
try:
    registerImag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src='images/mast_signon.gif']"))
        )
    ad_close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]"))
        ).ad_close_button.click()
    if registerImag:
        print("!Bienvenido a la página del registro¡")
        print("Por favor procede a llenar los campos")

    userName = driver.find_element(By.XPATH, "//input[contains(@name,'userName')]") 
    userName.send_keys("WB@gmail.com")
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[contains(@name,'password')]") 
    password.send_keys("Prueba.01")
    time.sleep(1)

    button = driver.find_element(By.XPATH, "//input[contains(@type,'submit')]") .click()
    time.sleep(2)

    confirmationMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Thank you for Loggin.')]"))
        )   
    
    if ad_close_button:
        print("publicidad encontrada")
        print(ad_close_button.text)
except Exception as e:
    print("publicidad no encontrada", e)

    if confirmationMessage:
        print("Mensaje de confirmación encontrado")
        print(confirmationMessage.text)
except Exception as e:
    print("Error al cargar la pagina de SIGN-ON", e)
    
finally:
    driver.close()