# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для инициализации URL и драйвера
    def __init__(self, url: str):
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    # Метод для открытия сайта по переданному URL
    def open_site(self):
        self.driver.get(self.url)

    # Метод для закрытия сайта
    def close_browser(self):
        time.sleep(2)
        self.driver.quit()


# Использование класса
test_instance = SauceDemoTest("https://www.saucedemo.com/")
test_instance.open_site()
test_instance.close_browser()
