from flask import Flask, jsonify, request, Response, json
#from requests import request
import requests
from products import products


app=Flask(__name__)

@app.route('/api')
def api():
    return jsonify({'mensaje':"hola prueba rest"})

@app.route('/products')
def getProducts():
    return jsonify({'productos': products, 'mensaje':'List of products'})

@app.route('/products/<string:productName>')
def getProduct(productName):
    encontrado=[product for product in products if product['name']==productName]
    if len(encontrado)>0:
        print(productName)
        return jsonify({"product":encontrado[0]})
    else:
        return jsonify({"mensaje":"article not found"}) 

@app.route('/products', methods=['POST'])
def addProducts():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product added succesfully ", "products": products})
    """r=request.json
    print(r)
    return 'received'"""

@app.route('/products/<string:productName>', methods=['PUT'])
def editProduct(productName):
    productFound=[product for product in products if product['name']==productName]
    if len(productFound)>0:
        productFound[0]['name']=request.json['name']
        productFound[0]['price']=request.json['price']
        productFound[0]['quantity']=request.json['quantity']
        return jsonify({"message":"Product updated", "product": productFound[0]})
    return jsonify({"message": "Product Not Found"})

@app.route('/products/<string:productName>', methods=['DELETE'])
def deleteProduct(productName):
    productsFound=[product for product in products if product['name']==productName]
    if len(productsFound)>0:
        products.remove(productsFound[0])
        return jsonify({"message":"Product deleted", "products": products})
    return jsonify({"message": "Product Not Found"})

@app.route('/sw')
def getPersonajes():
    apiUrl = 'https://swapi.dev/api/people/1'
    r=requests.request('GET',apiUrl)
    #print(r[0])
    return r.json()

if __name__ == '__main__':
    app.run(port=5000, debug=True)