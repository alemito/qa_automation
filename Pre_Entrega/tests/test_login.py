from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.funciones_login import login
import time

def test_login_saucedemo():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # Esperar hasta 5 segundos para que los elementos estén disponibles

    try:
        login(driver, "standard_user", "secret_sauce") # Usar la función de login desde funciones_login.py

        # Validar URL
        assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

        # Validar textos en pantalla
        titulo = driver.find_element(By.CLASS_NAME, "title").text
        logo = driver.find_element(By.CLASS_NAME, "app_logo").text

        assert titulo == "Products", "El título no es 'Products'"
        assert logo == "Swag Labs", "No aparece el texto 'Swag Labs'"

        print("Login exitoso y validaciones correctas")

    finally:
        time.sleep(2)
        driver.quit()
