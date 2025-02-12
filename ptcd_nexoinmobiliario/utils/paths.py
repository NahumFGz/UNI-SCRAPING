import os
import platform

##################################################
# 1. Definit las rutas del chrome driver
##################################################

# A. Definir sistema operativo
os_platform = platform.system().lower()

# B. Ruta donde se encuentra el proyecto
if os_platform == "darwin":
    BASE_PATH = "/Volumes/Projects/GitHubProjects/UNI-SCRAPING/chromedriver"

elif os_platform == "windows":
    BASE_PATH = "C:\GitHubProjets\JuegosDeMesaScrapper"

elif os_platform == "linux":
    BASE_PATH = "/home/data_brewanalytics/JuegosDeMesaScrapper"

# C. Definir rutas del chrome driver
if os_platform == "darwin":
    CHROMEDRIVER_PATH = os.path.join(BASE_PATH, "chromedriver", "darwin", "chromedriver")

elif os_platform == "windows":
    CHROMEDRIVER_PATH = os.path.join(BASE_PATH, "chromedriver", "windows", "chromedriver.exe")

elif os_platform == "linux":
    CHROMEDRIVER_PATH = os.path.join(BASE_PATH, "chromedriver", "linux", "chromedriver")

# D. Imprimir variables
print("ESTAMOS EN ---> ", os_platform)
print("BASE_PATH: ", BASE_PATH)
print("CHROME_DRIVER_PATH: ", CHROMEDRIVER_PATH)
print("")
