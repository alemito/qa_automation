from selenium import webdriver
from utils.funciones_login import login
from utils.funciones_catalogo import validar_titulo,validar_elementos_interfaz,verificar_producto_visible
import time

def test_catalogo_saucedemo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Esperar hasta 5 segundos por los elementos

    try:
        # Iniciar sesión antes de validar el catálogo
        login(driver, "standard_user", "secret_sauce")

        # Validar título, interfaz y primer producto
        validar_titulo(driver)
        validar_elementos_interfaz(driver)
        verificar_producto_visible(driver)

        print("Verificación del catálogo completada correctamente")

    finally:
        driver.quit()
