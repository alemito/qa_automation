# Proyecto de Automatización QA — Login en SauceDemo

Este proyecto forma parte de la **Pre-Entrega del curso de Automation QA**, y consiste en automatizar el proceso de login en el sitio [https://www.saucedemo.com](https://www.saucedemo.com), verificando que el acceso sea exitoso y que se muestren los elementos correspondientes en la página de inventario.

---

## Objetivo del Proyecto

Automatizar la prueba de login en el sitio **saucedemo.com**, utilizando:

- **Python** como lenguaje principal
- **Selenium WebDriver** para la automatización del navegador
- **Pytest** para la estructura y ejecución de pruebas
- **Git y GitHub** para control de versiones

---


## Instalación y Configuración

1. **Clonar el repositorio**
```bash
git clone https://github.com/alemito/qa_automation.git
cd qa_automation/Pre_Entrega
```
2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

---

## Puntos del TP
1. **Automatización de Login**

Ejecutar las pruebas con Pytest:
```bash
pytest -v tests/test_login.py
```

2. **Navegación y Verificación del Catálogo**

Ejecutar las pruebas con Pytest:
```bash
pytest -v tests/test_catalogo.py
```

2. **Interacción con Productos**

Ejecutar las pruebas con Pytest:
```bash
pytest -v tests/test_carrito.py
```