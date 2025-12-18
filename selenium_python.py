# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
menu = driver.find_element(By.ID, 'react-burger-menu-btn')
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')

# Выполняем действия и логируем
user_name.send_keys('standard_user')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('secret_sauce')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

# Метод click() для осуществления клика по кнопке
time.sleep(2)
button_login.click()    # Клик по кнопке login
print("Click Login Button")

menu.click()    # Клик по кнопке меню

time.sleep(2)
logout_button.click()   # Клик по кнопке logout

# Автоматическое закрытие сайта через 6 сек
time.sleep(3)
driver.close()
