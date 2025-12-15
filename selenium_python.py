# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Аргумент для запуска браузера в headless режиме (не открывая браузер)
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Базовый URL для открытия
base_url: str = 'https://www.saucedemo.com/'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.set_window_size(1920, 1080)

# Переменные, с помощью которых будет осуществляться поиск локаторов
user_name = driver.find_element(By.ID, 'user-name')
user_password = driver.find_element(By.ID, 'password')
button_login = driver.find_element(By.ID, 'login-button')

# Выполняем действия и логируем
user_name.send_keys('visual_user')  # Метод send_keys() для автоматического заполнения поля "Username"
print("Input Login")

user_password.send_keys('qwerty')  # Метод send_keys() для автоматического заполнения поля "Password"
print("Input Password")

button_login.click()  # Метод click() для осуществления клика по кнопке
print("Click Login Button")

# Уникальное название скриншота
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
name_screenshot = 'screenshot' + now_date + '.png'

# Метод для скриншота окна браузера
driver.save_screenshot('C:\\Users\\varenka\\repositories\\selenium_python\\screen\\' + name_screenshot)
print("Скриншот сохранён в папке 'screen'")

# Дополнительная проверка на текст
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")

value_warning_text = warning_text.text  # Создадим переменную

assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service', (
    f"""Ошибка: ожидается сообщение 'Epic sadface: Username and password do not match any user in this service',
    но получено '{value_warning_text}'"""  # Сравнение сообщения с ожидаемым результатом и
)
print("Сообщение корректно.")  # вывод текста об успешном прохождении проверки

# Автоклик по крестику в сообщении об ошибке
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print("Click Error Button")

time.sleep(6)
driver.close()
