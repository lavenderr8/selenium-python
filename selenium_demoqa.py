# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
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
base_url: str = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'

# Команда get для открытия ссылки
driver.get(base_url)

# Кликнем по нашему Drop Down
click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
time.sleep(2)
click_drop.click()

# Выберем элемент из списка и кликнем по нему
select_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'][7])")
time.sleep(2)
select_country.click()

# Закрываем браузер
time.sleep(3)
driver.close()
