# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import time
from selenium.webdriver import ActionChains
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
base_url: str = 'https://the-internet.herokuapp.com/horizontal_slider'

# Команда get для открытия ссылки
driver.get(base_url)

# Объект для взаимодействия с элементами
actions = ActionChains(driver)

# Находим ползунок и элемент, где отображается значение
slider = driver.find_element(By.XPATH, "//input[@type='range']")
slider_value_element = driver.find_element(By.ID, "range")

# Перемещаем ползунок на 2 пикселя
time.sleep(2)
actions.click_and_hold(slider).move_by_offset(2, 0).release().perform()

# Сравним значения ползунка: фактическое и отображаемое на странице
actual_value = slider.get_attribute("value")
displayed_value = slider_value_element.text

# Проверим, совпадают ли значения
assert actual_value == displayed_value, (
    f"Ошибка: значение ползунка ({actual_value}) "
    f"не совпадает с отображаемым ({displayed_value})"
)

print(f"Ползунок перемещён, текущее значение: {actual_value}")

# Закрываем браузер
time.sleep(3)
driver.close()
