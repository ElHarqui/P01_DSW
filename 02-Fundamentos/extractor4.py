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
    # Esperar dinámicamente a que los elementos con IDs estén presentes
    print("🔍 Iniciando búsqueda de elementos con IDs en la página...")
    todos_con_id = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@id]"))
    )
    print(f"✅ Búsqueda completada. Se encontraron {len(todos_con_id)} elementos con IDs.")

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

    # Verificar texto en elementos hijos y depurar HTML
    boton_clickeado = False
    for btn in botones_filtrados:
        texto = btn.get_attribute('innerText').strip()
        print(f"ID: {btn.get_attribute('id')} → Texto (innerText): '{texto}'")
        if texto:
            print(f"✅ Haciendo clic en ID: {btn.get_attribute('id')} con texto: '{texto}'")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn)).click()
            boton_clickeado = True
            break

    # Verificar atributos alternativos
    if not boton_clickeado:
        for btn in botones_filtrados:
            texto = btn.get_attribute('aria-label') or btn.get_attribute('title') or btn.get_attribute('alt')
            print(f"ID: {btn.get_attribute('id')} → Texto alternativo: '{texto}'")
            if texto:
                print(f"✅ Haciendo clic en ID: {btn.get_attribute('id')} con texto alternativo: '{texto}'")
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn)).click()
                boton_clickeado = True
                break

    # Intentar hacer clic en el primer botón filtrado como último recurso
    if not boton_clickeado:
        print("⚠️ Intentando hacer clic en el primer botón filtrado como último recurso.")
        if botones_filtrados:
            print(f"✅ Haciendo clic en ID: {botones_filtrados[0].get_attribute('id')}")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(botones_filtrados[0])).click()
            boton_clickeado = True

    if not boton_clickeado:
        raise Exception("No se pudo hacer clic en ningún botón filtrado.")

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
        # ========================
        # CERRAR DRIVER
        # ========================
        print("✅ Tabla exportada correctamente.")
        tablas[0].to_excel("incidentes_extraidos.xlsx", index=False)
except Exception as e:
    print(f"❌ Error al extraer o exportar la tabla: {e}")
    print("⚠️ No se encontraron tablas en la página.")
finally:
    driver.quit()
