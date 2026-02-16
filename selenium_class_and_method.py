# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для инициализация URL и драйвера
    def __init__(self, url: str):
        self.url = url
        self.driver = self._init_driver()  # Инициализация драйвера через статический метод

    # Статический метод для создания и настройки драйвера
    @staticmethod
    def _init_driver() -> webdriver.Chrome:
        # Настраиваем опции браузера
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        # Создаём экземпляр драйвера
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        return driver

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
