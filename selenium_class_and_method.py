# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для запуска браузера и открытия сайта
    def select_product(self):
        # Создаем экземпляр Chrome WebDriver
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        # URL для открытия
        base_url: str = "https://www.saucedemo.com/"

        # Открываем сайт
        self.driver.get(base_url)

        # Закрываем браузер
        time.sleep(3)
        self.driver.quit()


# Создаём экземпляр класса
start_test = SauceDemoTest()

# Вызываем метод
start_test.select_product()
