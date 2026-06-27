from flask import render_template
from . import agenda

@agenda.route("/agenda")
def agenda_home():

    eventos = []

    return render_template(
        "agenda.html",
        eventos=eventos
    )