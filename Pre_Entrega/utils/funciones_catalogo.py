from selenium.webdriver.common.by import By

def validar_titulo(driver):
    # Verificar que el título de la página sea "Products"
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products", "El título no es correcto"

def validar_elementos_interfaz(driver):
    # Verificar que existan el menú lateral y el filtro de productos
    driver.find_element(By.ID, "react-burger-menu-btn")
    driver.find_element(By.CLASS_NAME, "product_sort_container")

def verificar_producto_visible(driver):
    # Obtener el primer producto visible y mostrar su nombre y precio
    producto = driver.find_element(By.CLASS_NAME, "inventory_item")
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - Precio: {precio}")
