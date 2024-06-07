from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.pages.base_page import BasePage

class HomePage(BasePage):
        
    def open_google(self):
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()

    def search_for(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    def verify_search_result(self, expected_result):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//h3[contains(.,'{expected_result}')]"))
        )