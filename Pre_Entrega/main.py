"""
Acordarme de sacar los time hardcodeados
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5) # Esperar hasta 5 segundos para que los elementos estén disponibles

try:
    """
    Punto 1: Automatización del login

    Navegar a la página de login de saucedemo.com
    Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    Validar login exitoso verificando que se haya redirigido a la página de inventario

    Criterios mínimos:

    Login automatizado con espera explícita y validación de /inventory.html y “Products/Swag Labs”.

    """

    driver.get('https://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user') # Usar By.ID para localizar el campo de usuario
    driver.find_element(By.ID, 'password').send_keys('secret_sauce') # Usar By.ID para localizar el campo de contraseña
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click() # Usar By.CSS_SELECTOR para localizar el botón de inicio de sesión

    # Validacion de la redireccion
    assert '/inventory.html' in driver.current_url, "No se redirigió a la página de inventario"

    """
    Punto 2: Navegación y Verificación del Catálogo

    Navegar a la página de login de saucedemo.com
    Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
    Validar login exitoso verificando que se haya redirigido a la página de inventario

    """


    time.sleep(5)
finally:
    driver.quit()