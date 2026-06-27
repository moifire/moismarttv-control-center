import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "MoiSmartTV2026"

    DEBUG = True

    HOST = "0.0.0.0"

    PORT = 5000

    DATABASE = os.path.join(BASE_DIR, "database", "database.db")

    OUTPUT = os.path.join(BASE_DIR, "output")

    CACHE = os.path.join(BASE_DIR, "cache")

    LOGOS = os.path.join(BASE_DIR, "static", "logos")

    BACKDROPS = os.path.join(BASE_DIR, "static", "images")

    GITHUB_USER = ""

    GITHUB_REPO = ""

    GITHUB_TOKEN = ""

    TMDB_API = ""

    FANART_API = ""