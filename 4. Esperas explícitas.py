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
# abrir la pagina de Youtube y maximizar la pestaña
driver.maximize_window()
driver.get('https://www.youtube.com/watch?v=I3G5YB6bp7o')  # Reemplaza VIDEO_ID con el ID del video
time.sleep(10)

try:
    # esperar hasta que el botón de "Eexpandir" de la descripción del video sea visible
    wait = WebDriverWait(driver, 15)
    # pausa para asegurarnos de que la página esté completamente cargada
    time.sleep(10)

    # XPath específico para el botón de expandir la descripción
    ver_mas_boton = wait.until(EC.element_to_be_clickable((By.XPATH, "//tp-yt-paper-button[@id='expand']")))

    # realizar un clic en el botón "Expandir" de la descripción del video
    ver_mas_boton.click()

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")
