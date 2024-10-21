from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# ruta correcta a ChromeDriver
driver_path = "C:/Users/Sebas/Documents/chromedriver.exe"
# servicio para ChromeDriver
service = Service(executable_path=driver_path)
# inicializar el WebDriver para Chrome usando el servicio
driver = webdriver.Chrome(service=service)
# abrir la pagina de w3schools y maximizar la pestaña
driver.maximize_window()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
time.sleep(3)

try:
    # cambia al iframe donde se encuentra el botón que dispara el alert
    driver.switch_to.frame("iframeResult")
    # busca el botón que dispara el alert usando XPath para hacer clic en él
    alerta = driver.find_element("xpath", "//button[@onclick='myFunction()']")
    alerta.click()
    # cambia el control al alert emergente y obtiene su texto
    alerta2 = driver.switch_to.alert
    print("Texto del alert:", alerta2.text)
    time.sleep(10)
    # acepta para cerrar el alert
    alerta2.accept()
    time.sleep(5)

    # abrir la pagina de w3schools para la otra prueba
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm3")
    # cambia al iframe donde se encuentra el botón que dispara el alert
    driver.switch_to.frame("iframeResult")
    # busca el botón que dispara el confirm dialog usando XPath y haz clic en él
    confirm = driver.find_element("xpath", "//button[@onclick='myFunction()']")
    time.sleep(5)
    confirm.click()
    # cambia el control al confirm dialog y obtiene su texto
    confirm2 = driver.switch_to.alert
    print("Texto del confirm:", confirm2.text)
    time.sleep(5)
    # acepta para cerrar el confirm dialog
    confirm2.accept()
    time.sleep(5)

    # abrir la pagina de w3schools para la otra prueba
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
    # cambia al iframe donde se encuentra el botón que dispara el alert
    driver.switch_to.frame("iframeResult")
    # busca el botón que dispara el prompt dialog usando XPath y haz clic en él
    prompt = driver.find_element("xpath", "//button[@onclick='myFunction()']")
    time.sleep(5)
    prompt.click()
    # cambia el control al prompt dialog y obtiene su texto
    prompt2 = driver.switch_to.alert
    print("Texto del prompt:", prompt2.text)
    time.sleep(5)
    # envía un texto al prompt dialog
    prompt2.send_keys("Sebas")
    time.sleep(10)
    # acepta para cerrar el prompt dialog
    prompt2.accept()    

    # Esperar para visualizar
    time.sleep(2)

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", e)
    time.sleep(10)

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")