from selenium.webdriver.common.by import By
import time

def login(driver, username, password):
    """
    Realiza el login en saucedemo.com con las credenciales provistas.
    """
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username) # Usar By.ID para localizar el campo de usuario
    driver.find_element(By.ID, "password").send_keys(password)  # Usar By.ID para localizar el campo de contraseña
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click() # Usar By.CSS_SELECTOR para localizar el botón de inicio de sesión