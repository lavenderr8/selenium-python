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
min_value = float(slider.get_attribute("min"))
max_value = float(slider.get_attribute("max"))
step = float(slider.get_attribute("step"))

# Получаем ширину ползунка в пикселях
slider_width = slider.size["width"]

# Получаем начальное значение ползунка
start_value = float(slider.get_attribute("value"))

# Считаем количество шагов
steps_count = (max_value - min_value) / step

# Считаем, сколько пикселей приходится на один шаг
pixels_per_step = slider_width / steps_count

# Перемещаем ползунок на 26 пикселей
pixels_to_move = 26
actions.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()

time.sleep(1)

# Если смещение меньше одного шага, значение не должно измениться
expected_value = start_value

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
