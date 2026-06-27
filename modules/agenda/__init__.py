from flask import Blueprint

agenda = Blueprint(
    "agenda",
    __name__,
    template_folder="../../templates"
)

from . import routes