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

## Estructura del Proyecto

Pre_Entrega/
│
├── src/
│ └── funciones_login.py # Contiene funciones auxiliares de login
│
├── tests/
│ └── test_login.py # Contiene los casos de prueba automatizados con pytest
│
├── requirements.txt # Librerías necesarias para ejecutar el proyecto
└── README.md # Este archivo

---

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio**
   git clone https://github.com/alemito/qa_automation.git
   cd qa_automation/Pre_Entrega

2. **Instalar dependencias**
    pip install -r requirements.txt


---

## Ejecución de las pruebas

Ejecutar las pruebas con Pytest:

pytest -v tests/test_login.py
