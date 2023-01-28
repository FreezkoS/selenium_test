from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#работа с webdriver
class BasePage:

    #получение драйвера и базовой ссылки
    def __init__(self, driver, base_url) -> str:
        self.driver = driver
        self.base_url = base_url

    #нахождение элемента по переданному локатору
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Не удается найти элемент по локатору {locator}")

    #нахождение элементов по переданному локатору
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Не удается найти элементы по локатору {locator}")

    #переход на сайт и проверка открытия
    def go_to_site(self):
        self.driver.get(self.base_url)
        if self.driver.title != None:
            print('\nсайт открылся')
            return self.driver.get(self.base_url)
        else:
            print('\nоткрытие сайта не произошло')
            return False

    #проверка, что открыл именно тот сайт, который мы хотели
    def site_opened(self):
        if self.base_url == self.driver.current_url:
            return True
        else:
            return False