from selenium.webdriver.common.by import By

def agregar_primer_producto_al_carrito(driver):
    # Buscar todos los productos disponibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    # Hacer clic en el botón del primer producto para añadirlo al carrito
    productos[0].find_element(By.TAG_NAME, 'button').click()

def verificar_carrito(driver):
    # Verificar que el contador del carrito muestre 1
    contador = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert contador == '1', "El carrito no muestra el número correcto de productos"

def abrir_carrito(driver):
    # Hacer clic en el ícono del carrito para abrir la página del carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

def validar_producto_en_carrito(driver):
    # Verificar que el producto añadido aparezca en el carrito
    producto = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
    print(f"Producto en el carrito: {producto}")
