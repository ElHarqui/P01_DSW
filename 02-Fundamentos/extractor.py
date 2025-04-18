import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


# URL del formulario de login
login_url = "https://central.bioritmo.com.br/tas/secure/login/form"

# Datos de acceso (reemplaza con los tuyos)
payload = {
    "username": "NOL.CLAUDIA",
    "password": "jp181818"
}

# Iniciamos una sesión para mantener cookies
session = requests.Session()

# Hacemos POST para loggearnos
response = session.post(login_url, data=payload)

# Si el login fue exitoso, accedemos a la página con la tabla
pagina_datos = session.get("https://central.bioritmo.com.br/tas/secure/mango/window/2?t=1744925674009")

# Leer HTML usando StringIO para evitar el warning
html_data = StringIO(pagina_datos.text)
tablas = pd.read_html(html_data)

# Guardar la primera tabla
tablas[0].to_excel("tabla_extraida.xlsx", index=False)
print("✅ Tabla exportada exitosamente.")
