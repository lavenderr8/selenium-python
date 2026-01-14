# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
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
base_url: str = 'https://demoqa.com/date-picker'

# Команда get для открытия ссылки
driver.get(base_url)

# Находим поле ввода даты
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# Очищаем поле
time.sleep(2)
date_input.send_keys(Keys.CONTROL + "a")
time.sleep(2)
date_input.send_keys(Keys.DELETE)

# Создадим дату на 10 дней позже
time.sleep(2)
later_date = datetime.now() + timedelta(days=10)
formatted_date = later_date.strftime("%m/%d/%Y")

# Вводим дату в поле
date_input.send_keys(formatted_date)
date_input.send_keys(Keys.ENTER)

# Закрываем браузер
time.sleep(3)
driver.close()
