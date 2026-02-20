# Импортируем необходимые библиотеки
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Передаём драйвер из основного теста
    def __init__(self, driver):
        self.driver = driver

    # Метод авторизации пользователя
    def authorization(self, username: str, password: str):
        user_name = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
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
