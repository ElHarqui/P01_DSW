from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO
import pandas as pd
import time
import re

# ========================
# CONFIGURACIÓN DEL DRIVER
# ========================
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Descomenta si deseas ejecutar sin navegador
driver = webdriver.Chrome(options=chrome_options)

# ========================
# INGRESO AL LOGIN
# ========================
driver.get("https://central.bioritmo.com.br/tas/secure/login/form")
wait = WebDriverWait(driver, 20)

# Login
wait.until(EC.presence_of_element_located((By.NAME, "form_username"))).send_keys("NOL.CLAUDIA")
driver.find_element(By.NAME, "form_password").send_keys("jp181818", Keys.RETURN)

# ========================
# DETECTAR BOTÓN DE INCIDENTES (por ID)
# ========================
try:
    time.sleep(5)  # Esperar que cargue el DOM
    # Buscar todos los elementos que tengan un ID
    todos_con_id = driver.find_elements(By.XPATH, "//*[@id]")

    print("🧪 Todos los IDs encontrados en la página:")
    for el in todos_con_id:
        el_id = el.get_attribute("id")
        if el_id:
            print(f" - {el_id}")

    # Ahora filtrar los que se parezcan al patrón esperado
    botones_filtrados = []
    for el in todos_con_id:
        el_id = el.get_attribute("id")
        if el_id and re.search(r"^c6[A-Z0-9]{2}_[A-Z0-9]+$", el_id):
            botones_filtrados.append(el)

    print("\n🔍 IDs filtrados (coinciden con patrón relajado):")
    for btn in botones_filtrados:
        print(f" - {btn.get_attribute('id')}")


    if not botones_filtrados:
        raise Exception("No se encontraron IDs válidos según el patrón.")

    print("🔍 IDs filtrados según patrón:")
    for el in botones_filtrados:
        print(f" - {el.get_attribute('id')}")

    # Hacer clic en el primero con texto visible
    boton_clickeado = False
    for btn in botones_filtrados:
        texto = btn.text.strip()
        if texto:
            print(f"✅ Haciendo clic en ID: {btn.get_attribute('id')} con texto: '{texto}'")
            btn.click()
            boton_clickeado = True
            break

    if not boton_clickeado:
        raise Exception("Ningún botón tenía texto visible para hacer clic.")

except Exception as e:
    print("❌ No se pudo hacer clic en el botón de 'Incidentes de 1er nivel'")
    print(f"Error: {e}")
    driver.quit()
    exit()

# ========================
# ESPERAR CARGA DE LA TABLA
# ========================
time.sleep(6)

# ========================
# EXTRAER LA TABLA
# ========================
try:
    html = driver.page_source
    tablas = pd.read_html(StringIO(html))
    if tablas:
        tablas[0].to_excel("incidentes_extraidos.xlsx", index=False)
        print("✅ Tabla exportada correctamente.")
    else:
        print("⚠️ No se encontraron tablas en la página.")
except Exception as e:
    print(f"❌ Error al extraer o exportar la tabla: {e}")

# ========================
# CERRAR DRIVER
# ========================
driver.quit()
