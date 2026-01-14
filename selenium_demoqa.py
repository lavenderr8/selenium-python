# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time

from selenium.webdriver import ActionChains  # Импортируем ActionChains для выполнения действий мыши
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

# Базовый URL для открытия
base_url: str = 'https://demoqa.com/buttons'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.set_window_size(1920, 1080)

# Объект для выполнения действий мыши
action = ActionChains(driver)

# Находим кнопку для двойного клика
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# Выполняем двойной клик по кнопке и выводим сообщение о выполнении
action.double_click(double_click_button).perform()
print("Произведён двойной клик")

# Находим кнопку для клика правой кнопкой мыши
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
time.sleep(2)
# Выполняем клик правой кнопкой мыши и выводим сообщение о выполнении
action.context_click(right_click_button).perform()
print("Произведён клик по правой кнопке мыши")

# Закрываем браузер
time.sleep(3)
driver.close()
