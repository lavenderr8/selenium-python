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
driver.set_window_size(1920, 1080)

# Переменные, с помощью которых будет осуществляться поиск локаторов
user_name = driver.find_element(By.ID, 'user-name')
user_password = driver.find_element(By.ID, 'password')
button_login = driver.find_element(By.ID, 'login-button')

# Метод, для автоматического заполнения полей конкретными значениями
user_name.send_keys("visual_user")
user_password.send_keys("secret_sauce")

# Метод click() для осуществления клика по кнопке
button_login.click()

# Опишем выполнение шагов с помощью функции print()
print("Input Login")
print("Input Password")
print("Click Login Button")

# Выведем на печать наш url
print(driver.current_url)

# И сохраним url в переменную
get_url = driver.current_url

# Переменная с адресом нашей страницы
url = 'https://www.saucedemo.com/inventory.html'

# Сравнение ожидаемого результата и фактического с помощью оператора assert
assert url == get_url

# Визуальное подтверждение успешного прохождения проверки
print("URL корректен")

# Проверим дополнительно, что находимся на странице каталога
text_products = driver.find_element(By.XPATH, "//span[@class='title']")

value_text_products = text_products.text    # Создадим переменную и
print(value_text_products)                  # выведем текст заголовка

assert value_text_products == 'Products'    # Сравнение заголовка с ожидаемым результатом и
print("Заголовок корректен")                # вывод текста об успешном прохождении проверки

# Автоматическое закрытие сайта через 10 сек.
time.sleep(10)
driver.close()
