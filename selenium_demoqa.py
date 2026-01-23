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
base_url: str = 'https://demoqa.com/browser-windows'

# Команда get для открытия ссылки
driver.get(base_url)

# Находим кнопку New Tab и кликаем по ней
new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
time.sleep(2)
new_tab.click()

# Команда для открытия второй вкладки
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Возврат на первую вкладку
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

# Находим кнопку New Window и кликаем по ней
new_window = driver.find_element(By.XPATH, "//button[@id='windowButton']")
time.sleep(2)
new_window.click()

# Команда для открытия второго окна
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# Переключение на первое окно
driver.switch_to.window(driver.window_handles[0])

# Закрываем браузер
time.sleep(3)
driver.close()
