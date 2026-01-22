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
driver.find_element(By.XPATH, "//input[@id='sum1']").send_keys(str(first_value))
print(f"В первое поле введено значение: {first_value}")

# Вводим значение во второе поле
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='sum2']").send_keys(str(second_value))
print(f"Во второе поле введено значение: {second_value}")

# Клик по кнопке "Get Sum"
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='gettotal']/button").click()

# Сохранили значение, отображённое в поле "Result"
value_result = driver.find_element(By.XPATH, "//p[@id='addmessage']").text

# Проверка на соответствие ожидаемого результата с фактическим
assert value_result == str(sum_result), (
    f"Ожидаемый результат: '{sum_result}', но фактический: '{value_result}'"
)
print(f"Результат суммы: {value_result} – верно")

# Закрываем браузер
time.sleep(3)
driver.close()
