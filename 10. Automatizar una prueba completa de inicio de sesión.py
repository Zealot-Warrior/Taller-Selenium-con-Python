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
# abrir la pagina saucedemo y maximizar la pestaña
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(10)

try:
    # esperar a que el campo de nombre de usuario sea visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    # introducir el nombre de usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")
    time.sleep(10)
    # introducir la contraseña
    contraseña = driver.find_element(By.ID, "password")
    contraseña.send_keys("secret_sauce")
    time.sleep(10)
    # hacer clic en el botón de login
    boton = driver.find_element(By.ID, "login-button")
    boton.click()
    time.sleep(10)
    # verificar que se haya iniciado sesión correctamente
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", str(e))

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")