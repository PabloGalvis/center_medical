from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

# Rutas para gestión
#---------------POST-------------------
banca.add_url_rule(
    '/mock', view_func=controllers.mock, methods=['GET','POST','PUT','DELETE'])
# banca.add_url_rule(
#     '/mock2', view_func=controllers.mock2, methods=['GET'])


