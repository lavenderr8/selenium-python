# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# URL для открытия
base_url: str = 'https://www.saucedemo.com/'


# Функция для взаимодействия покупателя с меню
def menu(products: dict) -> str:
    print("Приветствую тебя в нашем интернет-магазине")
    print("Выбери один из следующих товаров и укажи его номер:\n")

    # Вывод списка товаров с их номерами и названиями
    for key, item in products.items():
        print(f"{key} - {item['description']}")

    # Цикл для корректного ввода пользователя
    while True:
        choice = input("Введите номер товара: ").strip()

        # Проверяем, что введённый номер есть в словаре товаров
        if choice in products:
            return choice

        else:
            print("Некорректный ввод. Попробуйте ещё раз.")


# Функция добавления товара в корзину
def add_to_cart(choice, products, driver):
    # Берём ID кнопки выбранного товара из словаря, находим по нему кнопку и кликаем по ней
    try:
        button_id = products[choice]["id_button"]
        time.sleep(2)
        driver.find_element(By.ID, button_id).click()

    # Если кнопка не найдена, выводим сообщение об ошибке
    except NoSuchElementException:
        print(f"Кнопка для товара {products[choice]['description']} не найдена!")


# Функция, проверяющая, что выбранный товар добавлен в корзину с правильным названием и ценой
def check_cart_item(choice, products, driver):
    # Переходим в корзину
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Ожидаемые данные
    expected_name = products[choice]["description"]
    expected_price = products[choice]["price"]

    # Фактические данные из корзины
    cart_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    # Проверки на соответствие ожидаемого названия и цены товара с фактическими
    assert cart_name == expected_name, f"""Название товара не совпадает!
                                           Ожидаемое: {expected_name}
                                           Фактическое: {cart_name}"""
    assert cart_price == expected_price, f"""Цена товара не совпадает!
                                             Ожидаемая: {expected_price}
                                             Фактическая: {cart_price}"""
    print(f"Товар {expected_name} по цене {expected_price} успешно добавлен в корзину✅")


# Функция заполнения данных о покупателе
def checkout(driver):
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()

    # Генерация данных покупателя
    first_name = fake.first_name()
    last_name = fake.last_name()
    postal_code = fake.postcode()

    # Заполняем форму
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(first_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(last_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(postal_code)

    # Нажимаем Continue
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()

    # Нажимаем Finish для завершения заказа
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(2)

    # Проверка успешного оформления заказа
    thank_you_text = driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
    assert thank_you_text == "Thank you for your order!", "Заказ не оформлен!"
    print("Заказ успешно оформлен✅")


# Команда get для открытия ссылки
driver.get(base_url)

fake = Faker()

# Авторизируемся
time.sleep(2)
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# Каталог товаров
product_catalog = {
    "1": {
        "description": "Sauce Labs Backpack",
        "price": "$29.99",
        "id_button": "add-to-cart-sauce-labs-backpack"
    },
    "2": {
        "description": "Sauce Labs Bike Light",
        "price": "$9.99",
        "id_button": "add-to-cart-sauce-labs-bike-light"
    },
    "3": {
        "description": "Sauce Labs Bolt T-Shirt",
        "price": "$15.99",
        "id_button": "add-to-cart-sauce-labs-bolt-t-shirt"
    },
    "4": {
        "description": "Sauce Labs Fleece Jacket",
        "price": "$49.99",
        "id_button": "add-to-cart-sauce-labs-fleece-jacket"
    },
    "5": {
        "description": "Sauce Labs Onesie",
        "price": "$7.99",
        "id_button": "add-to-cart-sauce-labs-onesie"
    },
    "6": {
        "description": "Test.allTheThings() T-Shirt (Red)",
        "price": "$15.99",
        "id_button": "add-to-cart-test.allthethings()-t-shirt-(red)"
    }
}

# Вызов функций
choice = menu(product_catalog)
add_to_cart(choice, product_catalog, driver)
check_cart_item(choice, product_catalog, driver)
checkout(driver)
