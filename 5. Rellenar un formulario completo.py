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
# abrir la pagina de fromulario en google y maximizar la pestaña
driver.maximize_window()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSckeYUbpg2g-OtV9ONoioNNa1DFxPoWJ8nFD6pcHzW7PnFCwA/viewform?usp=sf_link')  # Reemplaza VIDEO_ID con el ID del video
time.sleep(8)

try:
    # encontrar las casillas de cada uno de los cuadros de la encuesta, y escribir su respectiva información en ellas
    nombre = driver.find_element(By.XPATH, '//input[@aria-labelledby="i1"]')
    nombre.send_keys("Manuel")
    time.sleep(3)

    correo = driver.find_element(By.XPATH, '//input[@aria-labelledby="i5"]')
    correo.send_keys("Manuel@correo.com")
    time.sleep(3)

    direccion = driver.find_element(By.XPATH, '//textarea[@aria-labelledby="i9"]')
    direccion.send_keys("Av 20 #12")
    time.sleep(3)

    telefono = driver.find_element(By.XPATH, '//input[@aria-labelledby="i13"]')
    telefono.send_keys("1598732")
    time.sleep(3)

    comentarios = driver.find_element(By.XPATH, '//textarea[@aria-labelledby="i17"]')
    comentarios.send_keys("Desde la app")
    time.sleep(3)

    casilla = driver.find_element(By.XPATH, '//div[@aria-label="Si"]')
    casilla.click()
    time.sleep(3)
    # buscar la casilla de enviar y realizar un clic
    enviado = driver.find_element(By.XPATH, '//div[@aria-label="Submit"]')
    enviado.click()
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