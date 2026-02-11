# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


# Создаём общий класс для теста
class SauceDemoTest:

    # Метод для запуска браузера и выполнения теста
    def select_product(self):
        # Создаем экземпляр Chrome WebDriver
        self.driver: webdriver.Chrome = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        # URL для открытия
        base_url: str = "https://www.saucedemo.com/"

        # Открываем сайт
        self.driver.get(base_url)

        # Авторизируемся на сайте
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        time.sleep(2)
        user_name.send_keys("standard_user")
        print("Input Username")

        user_password = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        time.sleep(2)
        user_password.send_keys("secret_sauce")
        print("Input Password")

        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']")))
        time.sleep(2)
        login_button.click()
        print("Click Login Button")

        # Выбираем товар и переходим в корзину
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

        # Проверка, что мы находимся на странице корзины
        your_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        value_your_cart = your_cart.text
        assert value_your_cart == "Your Cart"
        print("Test Completed")

        # Закрываем браузер
        time.sleep(3)
        self.driver.quit()


# Создаём экземпляр класса
start_test = SauceDemoTest()

# Вызываем метод
start_test.select_product()
