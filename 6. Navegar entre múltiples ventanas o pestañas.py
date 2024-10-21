import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ruta correcta a ChromeDriver
driver_path = "C:/Users/Sebas/Documents/chromedriver.exe"
# servicio para ChromeDriver
service = Service(executable_path=driver_path)
# inicializar el WebDriver para Chrome usando el servicio
driver = webdriver.Chrome(service=service)
# abrir la pagina de Selenium y maximizar la pestaña
driver.maximize_window()
driver.get("https://selenium-python.readthedocs.io/installation.html")
time.sleep(3)

try:
    # buscar el enlace que deseas abrir en una nueva pestaña
    link = driver.find_element(By.XPATH, '//a[contains(text(),"https://sites.google.com/chromium.org/driver/")]')

    # abrir el enlace en una nueva pestaña usando JavaScript
    driver.execute_script("window.open(arguments[0], '_blank');", link.get_attribute('href'))

    # esperar unos segundos para que la nueva pestaña se abra
    time.sleep(3)

    # obtener los manejadores de todas las pestañas abiertas
    manejador = driver.window_handles

    # cambiar el foco a la nueva pestaña
    driver.switch_to.window(manejador[1])
    print("Cambio a la nueva pestaña.")

    # obtener el título de la página
    print("Título de la nueva pestaña:", driver.title)
    time.sleep(3)

    # volver a la pestaña original
    driver.switch_to.window(manejador[0])
    print("Regresó a la pestaña original.")
    time.sleep(3)

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")
