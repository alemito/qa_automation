from selenium import webdriver
from utils.funciones_login import login
from utils.funciones_catalogo import validar_titulo, validar_elementos_interfaz, verificar_producto_visible
from utils.funciones_carrito import agregar_primer_producto_al_carrito, verificar_carrito, abrir_carrito, validar_producto_en_carrito

def test_login_catalogo_carrito():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:

        # Punto 1: Login

        login(driver, "standard_user", "secret_sauce")
        assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"
        print("Login correcto")


        # Punto 2: Catálogo

        validar_titulo(driver)
        validar_elementos_interfaz(driver)
        verificar_producto_visible(driver)
        print("Catálogo verificado correctamente")


        # Punto 3: Carrito

        agregar_primer_producto_al_carrito(driver)
        verificar_carrito(driver)
        abrir_carrito(driver)
        validar_producto_en_carrito(driver)
        print("Carrito validado correctamente")

        print("Todas las pruebas se ejecutaron correctamente.")

    finally:
        driver.quit()
