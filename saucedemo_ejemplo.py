from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
print("Navegador iniciado")

try:
    # 1. Login en SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("✅ Login completado")

    # 2. Añadir producto al carrito
    nombre_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    driver.find_element(By.CSS_SELECTOR, ".btn_primary.btn_inventory").click()
    print(f"✅ Producto añadido: {nombre_producto}")

    # 3. Verificar carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"✅ Producto en carrito: {producto_en_carrito}")

    # 4. Finalizar compra
    driver.find_element(By.ID, "checkout").click()

    # Datos de envío
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Pérez")
    driver.find_element(By.ID, "postal-code").send_keys("28001")
    driver.find_element(By.ID, "continue").click()

    # Completar compra
    driver.find_element(By.ID, "finish").click()
    print("✅ Compra finalizada")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    # Esperar 10 segundos antes de cerrar el navegador
    print("Esperando 10 segundos antes de cerrar...")
    time.sleep(10)
    
    # Cerrar el navegador
    driver.quit()
    print("Navegador cerrado")