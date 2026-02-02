# Импортируем WebDriver, чтобы с ним взаимодействовать:
# открывать браузер и производить различные действия
import glob
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Путь к директории для скачивания файлов
path_download = "C:\\Users\\varenka\\repositories\\selenium_python\\files_download"

options = webdriver.ChromeOptions()

# Указываем директорию для скачивания файлов
prefs = {'download.default_directory': path_download}
options.add_experimental_option('prefs', prefs)

options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

# URL для открытия
base_url: str = 'https://www.lambdatest.com/selenium-playground/download-file-demo'

# Команда get для открытия ссылки
driver.get(base_url)

# клик по кнопке "Download File"
download_file_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
time.sleep(2)
download_file_button.click()
time.sleep(3)

# Имя ожидаемого файла
file_name: str = "LambdaTest.pdf"

# Формируем путь к файлу
file_path: str = os.path.join(path_download, file_name)

# Проверка, что файл скачался
assert os.access(file_path, os.F_OK) == True
print("Файл в директории")
time.sleep(2)

# Проверка, что файл не пустой
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

# Закрываем браузер
time.sleep(3)
driver.close()
