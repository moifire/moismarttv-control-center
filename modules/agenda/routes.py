from flask import render_template, jsonify

from . import agenda
from .service import AgendaService


@agenda.route("/agenda")
def agenda_home():

    eventos = []

    return render_template(
        "agenda.html",
        eventos=eventos
    )


@agenda.route("/api/agenda/update", methods=["POST"])
def update_agenda():

    try:

        eventos = AgendaService.update()

        return jsonify({
            "success": True,
            "events": len(eventos)
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500