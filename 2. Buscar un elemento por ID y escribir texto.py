from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

    # buscar la barra de búsqueda por su ID
    buscador = driver.find_element(By.ID, "APjFqb")

    # simular escribir en la barra de búsqueda
    buscador.send_keys("lol iron plays")

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")