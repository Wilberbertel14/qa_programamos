from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
Url = "https://demo.guru99.com/test/newtours/index.php"
User = "WB@gmail.com"
password ="Prueba.01"

def Register_Mercury():
    try:
        driver = webdriver.Chrome()
        driver.get(Url)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)

        
        driver.find_element(By.LINK_TEXT, "REGISTER").click()
        time.sleep(1)

        
        register_img = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='images/mast_register.gif']"))
        )

        if register_img:
            print("!Bienvenido a la página del registro¡")
            print("Por favor procede a llenar los campos")

        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)

        # Fill out the registration form
        driver.find_element(By.XPATH, "//input[contains(@id,'email')]").send_keys(User)
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[contains(@name,'password')]").send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[contains(@name,'confirmPassword')]").send_keys(password)
        time.sleep(1)

        # Submit the form
        driver.find_element(By.XPATH, "//input[@src='images/submit.gif']").click()
        time.sleep(2)

        # Wait for the confirmation message
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Note: Your user name is WB@gmail.com.')]"))
        )

        if confirmation_message:
            print("Mensaje de confirmación encontrado")
            print(confirmation_message.text)

    except Exception as e:
        print("Error al cargar la pagina de registro", e)

    finally:
        driver.quit()  # Ensure the browser is closed properly


# Call the function
Register_Mercury()

def SignOn_Mercury() :
    try:
        driver = webdriver.Chrome()
        driver.get(Url)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)

        #buttonRegister = driver.find_element(By.LINK_TEXT, "SIGN-ON") .click()
        #time.sleep(2)
 

        SignOnImag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@src='images/hdr_findflight.gif']"))
            )    
        if SignOnImag:
            print("!Bienvenido al modulo de Inicio de sesion¡")
            print("Por favor procede a llenar los campos")

        userName = driver.find_element(By.XPATH, "//input[contains(@name,'userName')]") .send_keys(User)
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[contains(@name,'password')]").send_keys(password)
        time.sleep(1)

        button = driver.find_element(By.XPATH, "//input[contains(@type,'submit')]") .click()
        time.sleep(2)

        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//b[contains(.,'Thank you for Loggin.')]"))
        )

        if confirmation_message:
            print("Mensaje de confirmación encontrado")
            print(confirmation_message.text)

    except Exception as e:
        print("Error al cargar la pagina de Sign on", e)

    finally:
        driver.quit()  # Ensure the browser is closed properly
        
SignOn_Mercury()    
