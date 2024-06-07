from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el navegador (asegúrate de tener el controlador adecuado para tu navegador)
driver = webdriver.Chrome()  # o webdriver.Firefox() si usas Firefox

try:
    # Navega a Google
    driver.get('https://www.google.com')

    # Encuentra el cuadro de búsqueda y busca la palabra "facebook"
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('facebook')
    search_box.send_keys(Keys.RETURN)

    # Espera a que los resultados se carguen y estén visibles
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(.,'Facebook - Inicia sesión o regístrate')]")))

    # Haz clic en el primer resultado
    first_result.click()

finally:
    # Cierra el navegador después de unos segundos
    driver.implicitly_wait(5)
    driver.quit()