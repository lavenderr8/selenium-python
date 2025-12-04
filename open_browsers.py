import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def open_site_in_browser(driver: webdriver):
    # Базовый URL для открытия
    base_url: str = 'https://www.saucedemo.com/'

    # Команда get для открытия ссылки
    driver.get(base_url)

    # Установка размеров окна браузера
    driver.set_window_size(1920, 1080)

    # Задержка, чтобы увидеть результат перед закрытием браузера через 10 сек.
    time.sleep(10)
    driver.close()


def open_in_chrome():
    """Запуск сайта в Google Chrome."""

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    open_site_in_browser(driver)


def open_in_firefox():
    """Запуск сайта в Mozilla Firefox."""

    driver = webdriver.Firefox(GeckoDriverManager().install())

    open_site_in_browser(driver)


def open_in_edge():
    """Запуск сайта в Microsoft Edge."""

    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    open_site_in_browser(driver)


if __name__ == "__main__":
    # Запуск по-очереди во всех трёх браузерах
    open_in_chrome()
    open_in_firefox()
    open_in_edge()
