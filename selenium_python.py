# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
import time

from selenium import webdriver
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
user_name.send_keys('standard_user')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('secret_sauce')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

button_login.click()  # Метод click() для осуществления клика по кнопке
print("Click Login Button")

# Добавление товаров и переход в корзину с помощью click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
driver.find_element(By.XPATH, "a[@data-test='shopping-cart-link']").click()

# Скроллинг с помощью наведения по локатору
actions = ActionChains(driver)
element = driver.find_element(By.ID, 'item_3_title_link')
actions.move_to_element(element).perform()

# Автоматическое закрытие сайта через 6 сек
time.sleep(6)
driver.close()
