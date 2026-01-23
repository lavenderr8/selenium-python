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
base_url: str = 'https://the-internet.herokuapp.com/javascript_alerts'

# Команда get для открытия ссылки
driver.get(base_url)

js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
time.sleep(2)
js_alert.click()
time.sleep(2)
print("Click for JS Alert")
driver.switch_to.alert.accept()

js_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
time.sleep(2)
js_confirm.click()
time.sleep(2)
print("Click for JS Confirm")
driver.switch_to.alert.dismiss()

js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
time.sleep(2)
js_prompt.click()
print("Click for JS Prompt")
time.sleep(2)
driver.switch_to.alert.send_keys("Hello")
driver.switch_to.alert.accept()

# Закрываем браузер
time.sleep(3)
driver.close()
