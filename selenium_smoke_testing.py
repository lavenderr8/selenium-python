# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для инициализация URL и драйвера
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

    # Метод для авторизации пользователя на сайте
    def login(self, username: str, password: str):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        time.sleep(2)
        user_name.send_keys(username)
        print("Input Username")

        user_password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        time.sleep(2)
        user_password.send_keys(password)
        print("Input Password")

        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        time.sleep(2)
        login_button.click()
        print("Click Login Button")

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
