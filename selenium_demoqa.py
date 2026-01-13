# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# Базовый URL для открытия
base_url: str = 'https://demoqa.com/radio-button'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.set_window_size(1920, 1080)

# Находим input радиокнопки "Impressive"
radio_input = driver.find_element(By.ID, "impressiveRadio")

# Находим label радиокнопки "Impressive" (позиционный XPath)
radio_label = driver.find_element(
    By.XPATH,
    "(//label[@class='custom-control-label'])[2]"
)

# Кликаем по radiobutton
radio_label.click()

# Проверяем состояние
if not radio_input.is_selected():
    print("Radio Button 'Impressive' unselected")
else:
    print("Radio Button 'Impressive' selected")

# Закрываем браузер
time.sleep(3)
driver.close()
