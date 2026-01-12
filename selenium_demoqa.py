# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные дествия
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
base_url: str = 'https://demoqa.com/checkbox'

# Команда get для открытия ссылки
driver.get(base_url)

# Установка размеров окна браузера
driver.set_window_size(1920, 1080)

# Найдём чек-бокс по локатору
check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")

# Выполним по нему клик
check_box.click()

# Проверим, что чек-бокс выбран и выведем сообщение об этом
if check_box.is_selected():
    print("Чек-бокс выбран")
else:
    print("Чек-бокс не выбран")

# Закрываем браузер
time.sleep(3)
driver.close()
