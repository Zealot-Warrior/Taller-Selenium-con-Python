from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ruta correcta a ChromeDriver
driver_path = "C:/Users/Sebas/Documents/chromedriver.exe"
# servicio para ChromeDriver
service = Service(executable_path=driver_path)
# inicializar el WebDriver para Chrome usando el servicio
driver = webdriver.Chrome(service=service)

try:
    # abrir la pagina google 
    driver.get("https://www.google.com")

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")