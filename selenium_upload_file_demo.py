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
base_url: str = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'

# Команда get для открытия ссылки
driver.get(base_url)

# Путь к файлу, который будем загружать
path_upload = "C:\\Users\\varenka\\repositories\\selenium_python\\file_upload\\screenshot2025.12.15-18.33.04.png"

# Название файла, после загрузки
file_name = "screenshot2025.12.15-18.33.04.png"

# Загружаем файл
select_file_button = driver.find_element(By.XPATH, "//input[@id='file']")
time.sleep(2)
select_file_button.send_keys(path_upload)
time.sleep(2)

# Получаем значение атрибута value у input
uploaded_file_value = select_file_button.get_attribute("value")

# Проверяем, что имя загруженного файла присутствует в value
if file_name in uploaded_file_value:
    print("Файл успешно загружен, имя файла отображается корректно")
else:
    print("Ошибка: имя загруженного файла не найдено")

# Закрываем браузер
time.sleep(3)
driver.close()
