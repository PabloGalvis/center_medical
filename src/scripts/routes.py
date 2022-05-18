from flask import Blueprint
from . import controllers

banca = Blueprint('banca', __name__)

# Rutas para gestión
#---------------POST-------------------
banca.add_url_rule(
    '/get_pasillos', view_func=controllers.get_pasillos, methods=['GET'])
banca.add_url_rule(
    '/get_sub_pasillos', view_func=controllers.get_sub_pasillos, methods=['GET'])
banca.add_url_rule(
    '/get_products_sub_pasillos', view_func=controllers.get_productos_sub_pasillos, methods=['GET'])
banca.add_url_rule(
    '/get_products_pasillos', view_func=controllers.get_productos_pasillos, methods=['GET'])
banca.add_url_rule(
    '/productos', view_func=controllers.productos, methods=['GET'])
banca.add_url_rule(
    '/set_compra_productos', view_func=controllers.set_compra_productos, methods=['POST'])
banca.add_url_rule(
    '/mock', view_func=controllers.mock, methods=['GET','POST','PUT','DELETE'])
# banca.add_url_rule(
#     '/mock2', view_func=controllers.mock2, methods=['GET'])


