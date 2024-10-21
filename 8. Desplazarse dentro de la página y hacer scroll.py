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
# abrir la pagina eltiempo y maximizar la pestaña
driver.maximize_window()
driver.get("https://www.eltiempo.com/")
time.sleep(6)

try:
    
    # realizar el scroll hasta el final de la página varias veces
    ultimo_scroll = driver.execute_script("return document.body.scrollHeight")

    while True:
        # desplazarse hacia abajo de la ventana
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # espera que se cargue el nuevo contenido
        time.sleep(2)

        # corroborar si se cargaron más elementos
        nuevo_scroll = driver.execute_script("return document.body.scrollHeight")
        if nuevo_scroll == ultimo_scroll:
            print("No se cargaron más elementos, terminando scroll.")
            break
        ultimo_scroll = nuevo_scroll

    time.sleep(6)
    # después de hacer scroll, buscar el último artículo con XPath
    ultimo_articulo = driver.find_element(By.XPATH, "(//article)[last()]")
    
    # obtiene el título y el enlace del artículo
    titulo = ultimo_articulo.find_element(By.XPATH, ".//h3[@class='c-article__title']/a").text  
    link = ultimo_articulo.find_element(By.XPATH, ".//h3[@class='c-article__title']/a").get_attribute('href')  
    
    
    # imprime la información del artículo
    print("Último elemento del periodico web encontrado:")
    print(f"Título: {titulo}")
    print(f"Enlace: {link}")
    time.sleep(6)

    print("ejecución satisfactoria")
    time.sleep(10)

except Exception as e:
    print("error de ejecución", str(e))

finally:
    # cerrar el navegador
    driver.quit()
    print("cerrando el navegador")