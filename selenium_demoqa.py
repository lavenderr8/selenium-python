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

# Находим ползунок
slider = driver.find_element(By.XPATH, "//input[@type='range']")

time.sleep(2)

# Получаем параметры ползунка
min_value = float(slider.get_attribute("min"))  # 0
max_value = float(slider.get_attribute("max"))  # 5
step = float(slider.get_attribute("step"))  # 0.5
slider_width = slider.size["width"]  # ширина в пикселях

# Получаем начальное значение
start_value = float(slider.get_attribute("value"))

# Считаем, сколько шагов у ползунка
steps_count = (max_value - min_value) / step

# Считаем, сколько пикселей занимает один шаг
pixels_per_step = slider_width / steps_count

# Перемещаем ползунок на 2 пикселя
pixels_to_move = 2
actions.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()

time.sleep(1)

# Считаем ожидаемое значение после перемещения
expected_value = start_value + (pixels_to_move / pixels_per_step) * step
expected_value = round(expected_value, 1)

# Получаем фактическое значение
actual_value = float(slider.get_attribute("value"))

# Проверяем, совпадает ли фактическое значение с ожидаемым
assert actual_value == expected_value, (
    f"Ошибка: ожидалось значение {expected_value}, "
    f"но получено {actual_value}"
)

print(f"Ползунок был {start_value}, стал {actual_value}")

# Закрываем браузер
time.sleep(3)
driver.close()
