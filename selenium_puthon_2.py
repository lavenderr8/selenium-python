# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium_python import user_name, user_password, button_login

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Базовый URL для открытия
base_url: str = 'https://www.saucedemo.com/'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.set_window_size(1920, 1080)

# Автоматическое заполнение поля Username неверным значением
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('visual_user')
print("Input Login")
time.sleep(4)
user_name.send_keys(Keys.CONTROL + "a")  # Автоматическое нажатие комбинации клавиш: Ctrl + a
user_name.send_keys(Keys.BACKSPACE)  # Автоматическое нажатие клавиши Backspace

# Автоматическое заполнение поля Password неверным значением
user_password = driver.find_element(By.XPATH, "//input[@id='password']")
user_password.send_keys('secret_sauce')
print("Input Password")
time.sleep(4)
user_name.send_keys(Keys.CONTROL + "a")  # Автоматическое нажатие комбинации клавиш: Ctrl + a
user_password.send_keys(Keys.BACKSPACE)  # Автоматическое нажатие клавиши Backspace

# Автоматический клик по кнопке "Login"
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

# Функция задержки выполнения кода на 6 сек
time.sleep(6)

# Обновление страницы
driver.refresh()
print("Страница перезагружена")

# Закрыть страницу
driver.close()
