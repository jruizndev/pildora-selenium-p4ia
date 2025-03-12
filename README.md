# Píldora Selenium P4IA
Este repositorio contiene material de apoyo para la introducción a Selenium del Bootcamp de Inteligencia Artificial.

## ¿Qué es Selenium?
Selenium es un framework que permite automatizar acciones en navegadores web. Sus principales usos son:
-   Pruebas automatizadas de aplicaciones web
-   Web scraping (extracción de datos)
-   Automatización de tareas repetitivas en navegadores

## Instalación
### Preparar el entorno
```bash
# Crear un entorno virtual
python -m venv selenium_env
# Activar el entorno virtual
# En Windows:
selenium_env\Scripts\activate
# En macOS/Linux:
source selenium_env/bin/activate
```

### Instalar Selenium y WebDriver Manager
```bash
pip install selenium webdriver-manager
```

### Ejemplo básico
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Para Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Para Firefox
from webdriver_manager.firefox import GeckoDriverManager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Para Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Uso básico
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
```

## Conceptos básicos
### Localizadores de elementos
```python
from selenium.webdriver.common.by import By

# Por ID
elemento = driver.find_element(By.ID, "username")

# Por nombre de clase
elementos = driver.find_elements(By.CLASS_NAME, "producto")

# Por selector CSS
elemento = driver.find_element(By.CSS_SELECTOR, ".menu > .item")

# Por XPath
elemento = driver.find_element(By.XPATH, "//button[text()='Login']")
```

### Acciones principales
```python
# Escribir texto
elemento.send_keys("Hola mundo")

# Hacer clic
elemento.click()

# Obtener texto
texto = elemento.text

# Limpiar un campo de texto
elemento.clear()
```

### Navegación
```python
# Abrir una URL
driver.get("https://www.ejemplo.com")

# Retroceder
driver.back()

# Avanzar
driver.forward()

# Refrescar página
driver.refresh()
```

### Esperas en Selenium
Las esperas son esenciales en Selenium para sincronizar la automatización con los tiempos de carga de la página y sus elementos.

```python
# Importaciones necesarias
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

#### Tipos de esperas:

1. **Pausas fijas**
```python
# Detiene la ejecución durante un tiempo exacto
time.sleep(5)  # Pausa por 5 segundos

# Útil en demostraciones y depuración
try:
    # Tu código de Selenium aquí
finally:
    # Esperar antes de cerrar
    print("Esperando 10 segundos antes de cerrar...")
    time.sleep(10)
    driver.quit()
```

2. **Esperas implícitas**
```python
# Configura un tiempo máximo global para todos los elementos
driver.implicitly_wait(10)  # Espera hasta 10 segundos

# Se configura una vez al inicio del script
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
```

3. **Esperas explícitas**
```python
# Espera hasta que se cumpla una condición específica
elemento = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
elemento.click()

# Algunas condiciones comunes
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "elemento")))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "elemento")))
WebDriverWait(driver, 10).until(EC.title_contains("Texto del título"))
```

## Buenas prácticas
### Siempre cierra el navegador correctamente
```python
try:
    # Tu código de Selenium aquí
finally:
    driver.quit()  # Esto se ejecutará incluso si hay errores
```

### Maneja las excepciones
Para código simple e introductorio, puedes usar un manejo general de excepciones:
```python
try:
    # Tu código de Selenium aquí
    driver.find_element(By.ID, "elemento")
except Exception as e:
    print(f"Error: {e}")  # Muestra el tipo específico de error
finally:
    driver.quit()
```

Para código más avanzado, puedes capturar excepciones específicas:
```python
from selenium.common.exceptions import NoSuchElementException
try:
    driver.find_element(By.ID, "elemento")
except NoSuchElementException:
    print("No se encontró el elemento")
finally:
    driver.quit()
```

## Ejercicio de ejemplo: Automatización en SauceDemo
En el archivo `saucedemo_ejemplo.py` encontrarás un script que automatiza:
1. Inicio de sesión
2. Selección de producto
3. Verificación del carrito
4. Proceso de compra

## Recursos adicionales
-   [Documentación oficial de Selenium](https://www.selenium.dev/documentation/)
-   [Selenium con Python](https://selenium-python.readthedocs.io/)
-   [WebDriver Manager para Python](https://github.com/SergeyPirogov/webdriver_manager)

## Contenido del repositorio
-   `saucedemo_ejemplo.py`: Código del ejercicio práctico con SauceDemo
