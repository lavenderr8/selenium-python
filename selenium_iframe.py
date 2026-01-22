# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
base_url: str = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'

# Команда get для открытия ссылки
driver.get(base_url)

# Находим iframe
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

# Обращаемся к текстовому полю
input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[2]")

# Очищаем поле
time.sleep(2)
input_pole.send_keys(Keys.CONTROL + "a")
time.sleep(2)
input_pole.send_keys(Keys.DELETE)

# Вводим новый текст
new_text = "Selenium"
time.sleep(2)
input_pole.send_keys(new_text)

# Выделяем поле с новым текстом
time.sleep(2)
input_pole.send_keys(Keys.CONTROL + 'a')

# Нажимаем кнопку Bold
time.sleep(2)
driver.find_element(By.XPATH, "//button[@title='Bold']").click()
print("Click Bold Button")

# Нажимаем кнопку Italic
time.sleep(2)
driver.find_element(By.XPATH, "//button[@title='Italic']").click()
print("Click Italic Button")

# Получаем текст после форматирования
formatted_text = input_pole.text
print(f"Стилистически изменённый текст: {formatted_text}")

# Проверка, что текст не изменился
assert formatted_text == new_text, (
    f"Текст изменился: ожидалось '{new_text}', получено '{formatted_text}'"
)

print("Текст не изменился после редактирования")

# Закрываем браузер
time.sleep(3)
driver.close()
