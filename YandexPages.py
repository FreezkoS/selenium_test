import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SECOND_SEARCH_FIELD = (By.NAME, "text")
    LOCATOR_YANDEX_IMAGES = (By.CLASS_NAME, 'PopularRequestList-Preview')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-container")
    LOCATOR_FIRST_LINK = (By.XPATH, '// *[ @ id = "search-result"] / li[1] / div[1] / div[1] / a')
    LOCATOR_IMAGE = (By.CLASS_NAME, 'serp-item__link')
    LOCATOR_IMAGE_OPENED = (By.CLASS_NAME, 'Link_view_default')
    LOCATOR_BUTTON_NEXT = (By.XPATH, '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[4]/i')
    LOCATOR_BUTTON_BACK = (By.XPATH, '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/i')

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_suggest_table(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_SUGGEST, time=2)
        suggest_list = [x.text for x in all_list if len(x.text) > 0]
        if len(suggest_list) > 0:
            print('\nТаблица результатов поиска появляется')
            return suggest_list
        else:
            print('\nТаблица результатов поиска пуста')
            return None

    def check_first_link(self):

        link = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_LINK, time=2)
        if link.text == "Тензор — IT-компания | СБИС":
            link.click()
            print(f"Переход по ссылке {link.get_attribute('href')} компании Тензор осуществлен\n")
        else:
            link.click()
            print('Ссылка ведет на сайт, который не является Тензор\n')
        return link

    def click_on_the_search_images(self):
        links = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_IMAGES, time=2)
        links[0].click()
        time.sleep(2)
        return links

    def check_name_category(self):
        text = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SECOND_SEARCH_FIELD)
        text = text.get_attribute('value')
        if len(text) > 0:
            print("Категория в поле поиска присутствует")
            return text
        else:
            print("Категория в поле поиска отсутствует")
            return False

    def open_image(self):
        image = self.find_elements(YandexSeacrhLocators.LOCATOR_IMAGE, time=2)
        image[0].click()
        time.sleep(2)
        return image


    def check_opened_image(self):
        title_image = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_OPENED, time=2)
        title_first = title_image.get_attribute('text')
        if len(title_first) > 0:
            print("Картинка открылась")
            return title_first
        else:
            print("Картинка не открылась")
            return False

    def click_button_next_back(self):
        title_image = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_OPENED, time=2).get_attribute('text')
        button_next = self.find_element(YandexSeacrhLocators.LOCATOR_BUTTON_NEXT, time=2)
        button_next.click()
        title_image_next = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_OPENED, time=2).get_attribute('text')
        time.sleep(2)
        if title_image != title_image_next:
            print('Смена картинки произошла')
            button_back = self.find_element(YandexSeacrhLocators.LOCATOR_BUTTON_BACK, time=2)
            button_back.click()
            time.sleep(2)
            title_image_back = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_OPENED, time=2).get_attribute('text')
            if title_image == title_image_back:
                print('Удалось вернуться на прошлую картинку')
                return True
            else:
                print('На прошлую картинку не удалось вернуться')
                return False
        else:
            print('Смена картинки не произошла')
            return False






