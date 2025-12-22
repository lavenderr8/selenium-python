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

# Автоматическое заполнение полей
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('standard_user')  # Поле "Username"
print("Input Login")

user_password = driver.find_element(By.ID, 'password')
user_password.send_keys('secret_sauce')  # Поле "Password"
print("Input Password")

# Клик по кнопке 'Login'
button_login = driver.find_element(By.ID, 'login-button')
time.sleep(2)
button_login.click()
print("Click Login Button")

# Выведем название товара в каталоге
product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")  # Первый товар
value_product_1 = product_1.text
print(value_product_1)

product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")  # Второй товар
value_product_2 = product_2.text
print(value_product_2)

# Выведем цену товара
price_product_1 = driver.find_element(  # Первый товар
    By.XPATH,
    "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div"
)
value_price_product_1 = price_product_1
print(value_price_product_1)

price_product_2 = driver.find_element(  # Второй товар
    By.XPATH,
    "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div"
)
value_price_product_2 = price_product_2
print(value_price_product_2)

# Кликнем по кнопке 'Add to cart'
select_product_1 = driver.find_element(  # Первый товар
    By.XPATH,
    "//*[@id='add-to-cart-sauce-labs-backpack']"
)
select_product_1.click()
print("Select Product 1")

select_product_2 = driver.find_element(  # Второй товар
    By.XPATH,
    "//*[@id='add-to-cart-sauce-labs-bike-light']"
)
select_product_2.click()
print("Select Product 2")

# Перейдём в корзину
cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
time.sleep(2)
cart.click()
print("Click Cart")

# Проверим, совпадает ли название и цена товара в корзине с тем, что мы выбрали
cart_product_1 = driver.find_element(  # Название первого товара
    By.XPATH,
    "//*[@id='item_4_title_link']/div"
)
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Info Cart Product 1 Good!")

cart_product_2 = driver.find_element(  # Название второго товара
    By.XPATH,
    "//*[@id='item_0_title_link']/div"
)
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("Info Cart Product 2 Good!")

cart_price_product_1 = driver.find_element(  # Цена первого товара
    By.XPATH,
    "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div"
)
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert price_product_1 == value_cart_price_product_1
print("Info Cart Price Product 1 Good!")

cart_price_product_2 = driver.find_element(  # Цена второго товара
    By.XPATH,
    "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div"
)
value_cart_price_product_2 = cart_price_product_2.text
print(value_cart_price_product_2)
assert price_product_2 == value_cart_price_product_2
print("Info Cart Price Product 2 Good!")

# Кликаем по кнопке 'Checkout'
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
time.sleep(2)
checkout.click()
print("Click Checkout Butten")

# Автозаполнение формы данных о покупателе
first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name.send_keys('Voivode')
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name.send_keys('Wallachia')
print("Input Last Name")

postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
postal_code.send_keys('3')
print("Input Postal Code")

# Кликнем по кнопке 'Continue'
continue_button = driver.find_element(By.XPATH, "//*[@id='continue']")
time.sleep(2)
continue_button.click()
print("Click Continue Button")

# Проверка на соответствие название товара, цены товара и
finish_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div")  # Название первого товара
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("Info Finish Product 1 Good!")

finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")  # Название второго товара
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("Info Finish Product 2 Good!")

finish_price_product_1 = driver.find_element(  # Цена первого товара
    By.XPATH,
    "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div"
)
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("Info Finish Price Product 1 Good!")

finish_price_product_2 = driver.find_element(  # Цена второго товара
    By.XPATH,
    "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div"
)
value_finish_price_product_2 = finish_price_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print("Info Finish Price Product 2 Good!")

summary_price = driver.find_element(  # Сумма
    By.XPATH,
    "//*[@id='checkout_summary_container']/div/div[2]/div[6]"
)
value_summary_price = summary_price.text
print(value_summary_price)

price_1 = float(value_finish_price_product_1.replace("$", ""))
price_2 = float(value_finish_price_product_2.replace("$", ""))

expected_total = price_1 + price_2

item_total = f"Item total: ${expected_total:.2f}"
print(item_total)
assert value_summary_price == item_total
print("Total Summary Price Good!")

# Кликнем по кнопке 'Finish'
finish_button = driver.find_element(By.XPATH, "//*[@id='finish']")
time.sleep(2)
finish_button.click()
print("Click Finish Button")

# Автоматическое закрытие сайта через 6 сек
time.sleep(3)
driver.close()
