from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Conectar al WebDriver dentro del contenedor
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME
)

# Navegar a Google y obtener el título de la página
driver.get("https://www.google.com")
print("Título de la página:", driver.title)

# Tomar una captura de pantalla
driver.save_screenshot("/tmp/captura.png")

# Cerrar el navegador
driver.quit()
