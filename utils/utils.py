##################################
# 0. Librerías
##################################
import datetime
import json
import os
import platform
import time
import zipfile

import pandas as pd
import requests
import wget
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils.paths import PROJECT_PATH

# 0. Variables iniciales
TIME_SLEEP = 2
ITERATIONS = 4


######################################
# 1. Funciones del driver y proxy
######################################
def download_driver(path):

    # 1. Obtener la última versión del driver
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.get(url)
    version_number = response.text

    # 2. Costruir la url de descarga
    os_platform = platform.system().lower()
    print("Sistema operativo: ", os_platform)

    system_version = ""
    if os_platform == "windows":
        system_version = version_number + "/chromedriver_win32.zip"
        print("Estás utilizando Windows.")

    elif os_platform == "linux":
        system_version = version_number + "/chromedriver_linux64.zip"
        print("Estás utilizando Linux.")

    elif os_platform == "darwin":
        system_version = version_number + "/	chromedriver_mac_arm64.zip"
        print("Estás utilizando macOS.")

    else:
        print("No se pudo determinar el sistema operativo.")

    # 3. Descargar el driver y extraer el driver
    print("Descargando la versión: ", system_version)
    download_url = "https://chromedriver.storage.googleapis.com/" + system_version
    latest_driver_zip = wget.download(download_url, "chromedriver.zip")

    with zipfile.ZipFile(latest_driver_zip, "r") as zip_ref:
        zip_ref.extractall(path)  # you can specify the destination folder path here

    # 4. Eliminar el zip
    os.remove(latest_driver_zip)


def get_chrome_driver(chromedriver_path=None, print_view=False, headless=False):
    # Configurar las opciones de Selenium
    options = webdriver.ChromeOptions()

    options.add_argument("--no-sandbox")
    # options.add_argument("--start-maximized")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")

    if print_view:
        options.add_argument("--disable-print-preview")

    if headless:
        options.add_argument("--headless=new")

    if chromedriver_path is not None:
        print("Usando el chromedriver_path: {}".format(chromedriver_path))
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        print("Usando el chromedriver_path por defecto")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return driver


def stop_chrome_driver(driver, server, proxy):
    driver.quit()


##################################
# 3. Funciones de Selenium
##################################


def find_elements_decorator(func):
    def wrapper(driver, by, value, text):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((by, value)))
            func(driver, by, value, text)
            time.sleep(1)

        except:
            print(f"Ocurrió un error by: ({by}), value: ({value})")

    return wrapper


def find_element_decorator(func):
    def wrapper(driver, by, value):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((by, value)))
            func(driver, by, value)
            time.sleep(1)

        except:
            print(f"Ocurrió un error by: ({by}), value: ({value})")

    return wrapper


def login_decorator(func):
    def wrapper(driver, by, value, username, password):
        try:
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((by, value)))
            func(driver, by, value, username, password)
            time.sleep(1)

        except:
            print(f"Ocurrió un error by: ({by}), value: ({value})")

    return wrapper


@find_elements_decorator
def find_elements_and_click(driver, by, value, text):
    elements = driver.find_elements(by, value)
    for element in elements:
        if text in element.text:
            element.click()
            break


@find_element_decorator
def find_element_and_click(driver, by, value):
    driver.find_element(by, value).click()


@login_decorator
def login(driver, by, value, username, password):
    elementos = driver.find_elements("css selector", ".v-field__input")
    time.sleep(1)
    elementos[0].send_keys(username)
    elementos[1].send_keys(password)
    time.sleep(1)
    driver.find_element(by, value).click()
