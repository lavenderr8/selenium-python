# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# URL для открытия
base_url: str = 'https://www.saucedemo.com/'

# Команда get для открытия ссылки
driver.get(base_url)

# Установим язык, на котором будет происходить генерирование
fake = Faker("en_US")

# Получение рандомного имени с помощью библиотеки Faker
name = fake.first_name()
print(f"Сгенерированное имя: {name}")

# Ввод имени в поле Username
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
time.sleep(2)
username.send_keys(name)
print("Input Username")

# Закрываем браузер
time.sleep(3)
driver.close()
