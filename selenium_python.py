# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Базовый URL для открытия
base_url: str = 'https://www.saucedemo.com/'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.maximize_window()

# Переменные, с помощью которых будет осуществляться поиск локаторов
user_name = driver.find_element(By.ID, 'user-name')
user_password = driver.find_element(By.ID, 'password')
button_login = driver.find_element(By.ID, 'login-button')

# Выполняем действия и логируем
user_name.send_keys('qwerty')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('123456')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

# Выделение полей: логин и пароль- и удаление значения полей
time.sleep(3)

user_name.send_keys(Keys.CONTROL + "a")    # Для поля логин
user_name.send_keys(Keys.DELETE)

user_password.send_keys(Keys.CONTROL + "a")    # Для поля пароль
user_password.send_keys(Keys.DELETE)

time.sleep(3)
user_name.send_keys('standard_user')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('secret_sauce')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

time.sleep(2)
button_login.click()  # Метод click() для осуществления клика по кнопке
print("Click Login Button")

# Автоматическое закрытие сайта через 6 сек
time.sleep(3)
driver.close()
