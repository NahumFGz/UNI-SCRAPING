#########################
# 0. Librerías
#########################
import os
import platform

#########################
# 1. Definir variables
#########################

# A. Definir sistema operativo
os_platform = platform.system().lower()

# B. Ruta donde se encuentra el proyecto
if os_platform == "darwin":
    PROJECT_PATH = "/Users/nahumfg/Projects/GitHubProjects/JuegosDeMesaScrapper"

elif os_platform == "windows":
    PROJECT_PATH = "C:\GitHubProjets\JuegosDeMesaScrapper"

elif os_platform == "linux":
    PROJECT_PATH = "/home/data_brewanalytics/JuegosDeMesaScrapper"

# C. Definir rutas del chrome driver
if os_platform == "darwin":
    CHROMEDRIVER_PATH = os.path.join(PROJECT_PATH, "chromedriver", "darwin", "chromedriver")

elif os_platform == "windows":
    CHROMEDRIVER_PATH = os.path.join(PROJECT_PATH, "chromedriver", "windows", "chromedriver.exe")

elif os_platform == "linux":
    CHROMEDRIVER_PATH = os.path.join(PROJECT_PATH, "chromedriver", "linux", "chromedriver")

# D. Imprimir variables
print("ESTAMOS EN ---> ", os_platform)
print("PROJECT_PATH: ", PROJECT_PATH)
print("CHROME_DRIVER_PATH: ", CHROMEDRIVER_PATH)
print("")
