from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# ========================
# CONFIGURACIÓN DEL DRIVER
# ========================
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ejecutar sin navegador si lo deseas
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
# HACER CLIC EN EL MÓDULO DE INCIDENTES
# ========================
# Espera a que cargue el menú o sección
# Aquí necesitas identificar el botón o link que abres manualmente

try:
    # Ejemplo: buscar el botón por texto visible o por xpath
    botones = driver.find_elements(By.XPATH, "//*[starts-with(@id, 'c6') and contains(@id, '_7')]")
    for btn in botones:
        if "Incidentes" in btn.text:
            btn.click()
            break

    
#
#//*[@id="c6JY_7S"]
#//*[@id="c6JE_7S"] 
#//*[@id="c6HW_7R"] 
# c6MU_7S
#//*[@id="c6MU_7S"]
#a0 b0 c0 d0 e1 f10 h11 i10 j6 k2 l1
#a0 b0 c0 d0 e1 f10 h11 i10 j6 k2 l1
#a0 b0 c0 d0 e1 f10 h11 i10 j6 k2 l1
#c6L3_7R
#c6MU_7R
#//*[@id="c6L3_7S"]
except:
    print("❌ No se pudo hacer clic en el botón de 'Incidentes de 1er nivel'")
    driver.quit()
    exit()

# Esperar que cargue la tabla luego del clic
time.sleep(6)  # o mejor: usar WebDriverWait si conoces un selector de la tabla

# ========================
# EXTRAER LA TABLA
# ========================
html = driver.page_source
tablas = pd.read_html(html)

# Guardar la tabla
tablas[0].to_excel("incidentes_extraidos.xlsx", index=False)

print("✅ Tabla exportada correctamente.")

# ========================
# CERRAR DRIVER
# ========================
driver.quit()
