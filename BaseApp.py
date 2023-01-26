from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Не удается найти элемент по локатору {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Не удается найти элементы по локатору {locator}")

    def go_to_site(self):
        self.driver.get(self.base_url)
        if self.driver.title != None:
            return self.driver.get(self.base_url)
        else:
            return False

    def site_opened(self):
        if self.base_url == self.driver.current_url:
            return True
        else:
            return False