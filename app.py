from database.database import Database
from flask import Flask, render_template
from config import Config
import os

app = Flask(__name__)
from modules.agenda import agenda

app.register_blueprint(agenda)
app.config.from_object(Config)


# ------------------------
# Dashboard
# ------------------------
@app.route("/")
def dashboard():

    db = Database()

    stats = {

        "eventos": db.scalar(
            "SELECT COUNT(*) FROM events"
        ),

        "canales": db.scalar(
            "SELECT COUNT(*) FROM channels"
        ),

        "peliculas": db.scalar(
            "SELECT COUNT(*) FROM movies"
        ),

        "series": db.scalar(
            "SELECT COUNT(*) FROM series"
        ),

        "usuarios": 1,

        "ultima_actualizacion": "--:--"

    }

    db.close()

    return render_template(
        "dashboard.html",
        stats=stats
    )

# ------------------------
# Agenda
# ------------------------

# ------------------------
# IPTV
# ------------------------
@app.route("/iptv")
def iptv():
    return "<h2>IPTV (Próximamente)</h2>"


# ------------------------
# Stremio
# ------------------------
@app.route("/stremio")
def stremio():
    return "<h2>Stremio (Próximamente)</h2>"


# ------------------------
# Películas
# ------------------------
@app.route("/movies")
def movies():
    return "<h2>Películas (Próximamente)</h2>"


# ------------------------
# Series
# ------------------------
@app.route("/series")
def series():
    return "<h2>Series (Próximamente)</h2>"


# ------------------------
# Configuración
# ------------------------
@app.route("/settings")
def settings():
    return "<h2>Configuración (Próximamente)</h2>"


if __name__ == "__main__":

    app.run(
    host=Config.HOST,
    port=Config.PORT,
    debug=Config.DEBUG
)