# Импортируем необходимые библиотеки
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для инициализации URL и драйвера
    def __init__(self, url: str):
        self.url = url
        self.driver = self._init_driver()

        # Создаём объект страницы логина
        self.login_page = LoginPage(self.driver)

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

    # Метод авторизации
    def login(self, username: str, password: str):
        self.login_page.authorization(username, password)

    # Метод для выбора товара и перехода в корзину
    def add_product_to_cart(self):
        select_product = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        time.sleep(2)
        select_product.click()
        print("Click Add to cart")

        go_to_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        time.sleep(2)
        go_to_cart.click()
        print("Enter Shopping Cart")

    # Метод для проверки, что мы находимся на странице корзины
    def check_cart(self):
        your_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        value_your_cart = your_cart.text
        assert value_your_cart == "Your Cart"
        print("Test Completed")

    # Метод для закрытия сайта
    def close_browser(self):
        time.sleep(2)
        self.driver.quit()


# Использование класса
test_instance = SauceDemoTest("https://www.saucedemo.com/")
test_instance.open_site()
test_instance.login("standard_user", "secret_sauce")
test_instance.add_product_to_cart()
test_instance.check_cart()
test_instance.close_browser()
