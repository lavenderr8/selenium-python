# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
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
base_url: str = 'https://demoqa.com/dynamic-properties'

# Команда get для открытия ссылки
driver.get(base_url)

# Пробуем найти нужную нам кнопку, но получаем ошибку
try:
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
    button_visible.click()

# Указываем ожидаемое исключение
except NoSuchElementException:
    print("Элемент не найден: получен NoSuchElementException")
    time.sleep(5)
    driver.refresh()  # Обновляем страницу
    time.sleep(5)
    button_visible = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")  # Заново пытаемся найти кнопку
    button_visible.click()
    print("Click Visible After 5 Seconds Button")

# Закрываем браузер
time.sleep(3)
driver.close()
