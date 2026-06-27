from flask import render_template, jsonify

from . import agenda
from .service import AgendaService



@agenda.route("/api/agenda/update", methods=["POST"])
def update_agenda():

    eventos = AgendaService.update()

    return jsonify({

        "success": True,

        "events": len(eventos)

    })

@agenda.route("/agenda")
def agenda_home():

    eventos = []

    return render_template(
        "agenda.html",
        eventos=eventos
    )