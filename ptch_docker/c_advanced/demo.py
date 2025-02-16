# # A. Librerias y rutas

import io
import time

from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


# # B. Funciones
def get_chrome_driver(
    remote_url="http://localhost:4444/wd/hub", print_view=False, headless=False, download_path="/home/seluser/Downloads"
):

    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")

    # Configurar la ruta de descargas
    prefs = {
        "download.default_directory": download_path,  # Ruta personalizada para descargas
        "download.prompt_for_download": False,  # No preguntar antes de descargar
        "download.directory_upgrade": True,  # Actualizar directorio de descargas
        "safebrowsing.enabled": True,  # Evitar bloqueos de descargas peligrosas
    }
    options.add_experimental_option("prefs", prefs)

    # Argumentos opcionales
    if print_view:
        options.add_argument("--disable-print-preview")
    if headless:
        options.add_argument("--headless=new")

    # Configurar el driver remoto
    driver = webdriver.Remote(command_executor=remote_url, options=options)

    return driver


def take_screenshot(driver, image_name="screenshot.png", save_path="/home/seluser/Downloads"):
    screenshot = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(screenshot))
    full_path = f"{save_path}/{image_name}"
    image.save(full_path)


# # C. Prueba
if __name__ == "__main__":
    driver = get_chrome_driver()

    url = "https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/map_red_graf.php?cod=112163&estado=REAL&tipo_esta=M&cate=CO&cod_old="
    driver.get(url)
    take_screenshot(driver, image_name="1.png")
    time.sleep(1.5)

    # Click en el botón "Tabla" usando By.ID
    driver.find_element(By.ID, "tabl").click()
    take_screenshot(driver, image_name="2.png")
    time.sleep(1.5)

    # Extraer el html de la página
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Buscar el elemento del captcha por su tag y atributos característicos
    captcha_element = soup.find("span", {"style": "color: red; font-size:xxx-large"})
    if captcha_element:
        print("Captcha encontrado:", captcha_element.text)
    else:
        print("Captcha no encontrado")

    take_screenshot(driver, image_name="3.png")
    time.sleep(1.5)

    # Encontrar el campo de entrada del captcha por su ID
    captcha_input = driver.find_element(By.ID, "captchaInput")

    # Ingresar el texto del captcha
    captcha_input.send_keys(captcha_element.text)
    take_screenshot(driver, image_name="4.png")
    time.sleep(1.5)

    # Click en el botón "Verificar" usando By.ID
    driver.find_element(By.ID, "entrar").click()
    take_screenshot(driver, image_name="5.png")
    time.sleep(1.5)

    driver.switch_to.frame("contenedor")
    take_screenshot(driver, image_name="6.png")
    time.sleep(1.5)

    driver.find_element(By.ID, "export101").click()
    take_screenshot(driver, image_name="7.png")
    time.sleep(1.5)

    driver.quit()
