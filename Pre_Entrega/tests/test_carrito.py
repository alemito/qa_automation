from selenium import webdriver
from utils.funciones_login import login
from utils.funciones_carrito import agregar_primer_producto_al_carrito, verificar_carrito, abrir_carrito, validar_producto_en_carrito
import time

def test_carrito_saucedemo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Esperar hasta 5 segundos por los elementos

    try:
        # Login
        login(driver, "standard_user", "secret_sauce")

        # Agregar producto al carrito
        agregar_primer_producto_al_carrito(driver)

        # Verificar contador del carrito
        verificar_carrito(driver)

        # Abrir carrito y validar producto
        abrir_carrito(driver)
        validar_producto_en_carrito(driver)

        print("Prueba de carrito completada correctamente.")

    finally:
        time.sleep(2)
        driver.quit()
