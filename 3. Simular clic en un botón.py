from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ruta correcta a ChromeDriver
driver_path = "C:/Users/Sebas/Documents/chromedriver.exe"
# servicio para ChromeDriver
service = Service(executable_path=driver_path)
# inicializar el WebDriver para Chrome usando el servicio
driver = webdriver.Chrome(service=service)
# maximizar la pestaña 
driver.maximize_window()

try:
    # abrir la pagina google
    driver.get("https://www.google.com")

    # buscar la barra de búsqueda por su ID
    buscador = driver.find_element(By.ID, "APjFqb")

    time.sleep(10)

    # simular escribir en la barra de búsqueda
    buscador.send_keys("lol iron plays")

    time.sleep(5)

    # esperar a que el botón de búsqueda esté presente en el DOM y sea interactuable
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "btnK"))
    )

    # usar JavaScript para asegurarse de que el botón esté visible e interactuar con él
    driver.execute_script("document.getElementsByName('btnK')[0].click();")

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")