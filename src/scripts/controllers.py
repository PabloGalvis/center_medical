from .query import Query
from flask import request, jsonify, json

query_helper = Query()

def mock():
    try:
        query = query_helper.get_pasillos()
        return jsonify(query)
    except: print("fallo")
    # if(request.method == "POST"):
    #     print(222)
    # nombre = request.args.get('nombre',"paco")
    # json = request.json['json']
    return "SSS"

def mock2():
    return "hola mundo mock 2"
def get_pasillos():
    try:
        query = query_helper.get_pasillos()
        return jsonify(query)
    except: return jsonify("fallo conexion")
    # obj = [{'img': 'https://d50xhnwqnrbqk.cloudfront.net/featured/web/a4cf85a23b9d5ade6ef19e9835038781.jpg', 'titulo': 'Navidad'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/a02b5c8924c4d79a4caa6f47b3e89bd6.png', 'titulo': 'Lacteos'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/e310a83bd35f77683f5d78c86c9a9319.png', 'titulo': 'Carnes'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/065d0d7967f6eb5c36e23793a267265e.png', 'titulo': 'Galletas'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/a02b5c8924c4d79a4caa6f47b3e89bd6.png', 'titulo': 'Pasteleria'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/e310a83bd35f77683f5d78c86c9a9319.png', 'titulo': 'Aceites'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/featured/web/a4cf85a23b9d5ade6ef19e9835038781.jpg', 'titulo': 'Arroces'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/6f3f0c6f36df4a3d7396c40a9a5f4f6f.png', 'titulo': 'Pastas'},
    #     {'img': 'https://d50xhnwqnrbqk.cloudfront.net/stores/images/app/59902a4d93a37e24c1ca10486f2745b2.png', 'titulo': 'Vegetales'}]
    # return jsonify(
    #     obj
    # )
def get_sub_pasillos():
    idPasillo = request.args.get('idPasillo',"")
    try:
        query = query_helper.get_sub_pasillos(idPasillo)
        return jsonify(query)
    except: return jsonify("fallo conexion")

def get_productos_sub_pasillos():
    idSubPasillo = request.args.get('idSubPasillo',"")
    try:
        query = query_helper.get_productos_sub_pasillos(idSubPasillo)
        return jsonify(query)
    except: return jsonify("fallo conexion")

    
def get_productos_pasillos():
    idPasillo = request.args.get('idPasillo',"")
    try:
        query = query_helper.get_productos_pasillos(idPasillo)
        return jsonify(query)
    except: return jsonify("fallo conexion")
