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
base_url: str = 'https://lambdatest.com/selenium-playground/simple-form-demo'

# Команда get для открытия ссылки
driver.get(base_url)

# Создадим переменные с числовым значением и переменную их сложения
first_value = 88
second_value = 26
sum_result = first_value + second_value

# Вводим значение в первое поле
time.sleep(2)
input_first_value = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_first_value.send_keys(str(first_value))

# Вводим значение во второе поле
time.sleep(2)
input_second_value = driver.find_element(By.XPATH, "//input[@id='sum2']")
input_second_value.send_keys(str(second_value))

# Клик по кнопке "Get Sum"
time.sleep(2)
get_sum_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
get_sum_button.click()

# Сохранили значение, отображённое в поле "Result"
result = driver.find_element(By.XPATH, "//p[@id='addmessage']")

# Проверка на соответствие ожидаемого результата с фактическим
value_result = result.text
assert value_result == str(sum_result)
print("Значения совпадают")

# Закрываем браузер
time.sleep(3)
driver.close()
