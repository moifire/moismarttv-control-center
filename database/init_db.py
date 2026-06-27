import sqlite3
from config import Config
import os

# Crear carpeta database si no existe
os.makedirs(os.path.dirname(Config.DATABASE), exist_ok=True)

conn = sqlite3.connect(Config.DATABASE)
cursor = conn.cursor()

# -----------------------
# Eventos
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    date TEXT,
    time TEXT,

    sport TEXT,

    competition TEXT,

    title TEXT,

    channel TEXT,

    backdrop TEXT,

    source TEXT

)
""")

# -----------------------
# Eventos Manuales
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS manual_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    date TEXT,
    time TEXT,

    sport TEXT,

    competition TEXT,

    title TEXT,

    channel TEXT,

    backdrop TEXT

)
""")

# -----------------------
# Canales IPTV
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS channels (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    logo TEXT,

    url TEXT,

    category TEXT

)
""")

# -----------------------
# Películas
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    year INTEGER,

    poster TEXT,

    category TEXT

)
""")

# -----------------------
# Series
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS series (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    poster TEXT,

    season INTEGER,

    episode INTEGER

)
""")

# -----------------------
# Configuración
# -----------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    value TEXT

)
""")

conn.commit()
conn.close()

print("✅ Base de datos creada correctamente.")