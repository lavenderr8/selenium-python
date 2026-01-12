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

# Выполняем действия и логируем
user_name.send_keys('standard_user')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('secret_sauce')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

time.sleep(2)
button_login.click()  # Метод click() для осуществления клика по кнопке
print("Click Login Button")

# Добавляем товар в корзину и переходим в корзину
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@data-test='shopping_cart_link']").click()

# Кликаем по кнопке "Назад"
time.sleep(2)
driver.back()
print("Go Back")

# Кликаем по кнопке "Вперёд"
time.sleep(2)
driver.forward()
print("Go Forward")

# Автоматическое закрытие сайта через 6 сек
time.sleep(3)
driver.close()
