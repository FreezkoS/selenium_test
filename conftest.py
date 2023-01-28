import pytest
from selenium import webdriver

#настройка состояния системы на проведения тестирования
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()