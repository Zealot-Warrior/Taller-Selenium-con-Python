from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ruta correcta a ChromeDriver
driver_path = "C:/Users/Sebas/Documents/chromedriver.exe"
# servicio para ChromeDriver
service = Service(executable_path=driver_path)
# inicializar el WebDriver para Chrome usando el servicio
driver = webdriver.Chrome(service=service)
# abrir la pagina postman y maximizar la pestaña
driver.maximize_window()
driver.get("https://www.postman.com/")

try:

    # esperar a que la página cargue completamente
    time.sleep(5) 
    # tomar la primera captura de pantalla y envia un mensaje a la consola
    pantallazo1 = "pantalla_1.png"
    driver.save_screenshot(pantallazo1)
    print(f"Captura de pantalla 1 guardada en: {pantallazo1}")
    time.sleep(10)

    # desplazarse ligeramente hacia abajo
    driver.execute_script("window.scrollBy(0, 300);")  # Desplazarse 300 píxeles hacia abajo
    time.sleep(2)  # Esperar un poco para asegurarse de que la página se haya ajustado

    # tomar la segunda captura de pantalla y envia un mensaje a la consola
    pantallazo2 = "pantalla_2.png"
    driver.save_screenshot(pantallazo2)
    print(f"Captura de pantalla 2 guardada en: {pantallazo2}")

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", str(e))

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")