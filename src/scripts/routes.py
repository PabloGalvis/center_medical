from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

# Rutas para gestión
#---------------POST-------------------
banca.add_url_rule(
    '/mock', view_func=controllers.mock, methods=['GET','POST','PUT','DELETE'])
# banca.add_url_rule(
#     '/mock2', view_func=controllers.mock2, methods=['GET'])
banca.add_url_rule(
    '/users', view_func=controllers.users, methods=['GET','POST','PUT','DELETE'])
banca.add_url_rule(
    '/usersLocal', view_func=controllers.usersLocal, methods=['GET','POST','PUT','DELETE'])
banca.add_url_rule(
    '/maps', view_func=controllers.maps, methods=['GET','POST','PUT','DELETE'])
banca.add_url_rule(
    '/placeHolder', view_func=controllers.placeHolder, methods=['GET'])
banca.add_url_rule(
    '/placeHolder', view_func=controllers.placeHolderInsert, methods=['POST'])
banca.add_url_rule(
    '/placeHolder', view_func=controllers.placeHolderUpdate, methods=['PUT'])
banca.add_url_rule(
    '/doctor', view_func=controllers.doctor, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/paciente', view_func=controllers.paciente, methods=['GET,POST,PUT'])
banca.add_url_rule(
    '/diagnostico', view_func=controllers.diagnostico, methods=['GET,POST,PUT'])



