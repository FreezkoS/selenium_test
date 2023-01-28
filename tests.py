from YandexPages import SearchHelper
import time

#ЗАДАНИЕ1 проведение тестирования сайта Тензор
def test_tensor_site(browser):
    yandex_main_page = SearchHelper(browser, 'https://ya.ru/')
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("тензор")
    time.sleep(2) #задержка, чтобы не появилась капча
    yandex_main_page.check_suggest_table()
    time.sleep(1)
    yandex_main_page.click_on_the_search_button()
    time.sleep(1)
    yandex_main_page.check_first_link()


#ЗАДАНИЕ2 проведение тестирования яндекс картинок
def test_images(browser):
    yandex_main_page = SearchHelper(browser, 'https://yandex.ru/images')
    yandex_main_page.go_to_site()
    yandex_main_page.site_opened()
    yandex_main_page.click_on_the_search_images()
    yandex_main_page.check_name_category()
    yandex_main_page.open_image()
    yandex_main_page.check_opened_image()
    yandex_main_page.click_button_next_back()



