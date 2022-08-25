from flask import request, Flask, flash, render_template, jsonify, url_for, session, make_response, g
import database as bd
from forms import Producto
from settings.config import configuration

app= Flask(__name__)

app.config.from_object(configuration)

@app.route('/')
def api():
    session['usuario']='Luis Guillermo'
    visited=request.cookies.get('visited')
    if visited=='True':
        return render_template('index.html', titulo='Ejemplo SQLite-thanks for coming')
        
    else:
        response=make_response(render_template('index.html', titulo='Ejemplo SQLite-new user'))
        response.set_cookie('visited', 'True')
        response.set_cookie('language','es')
        return response
    #return render_template('index.html', titulo='Ejemplo SQLite')

#uso del decorador before_request que pertenece a los decoradores de peticion
@app.before_request
def before_request():
    if 'usuario' in session:
        g.elusuario='luis10'
    else:
        g.elusuario=None

@app.route('/cerrar')
def cerrar():
    flash('Sesion cerrada')
    session.clear()
    return render_template('cerrando.html', titulo='Ejemplo SQLite')

@app.route('/productos')
def getProducts():
    lista_productos = bd.sql_select_products()
    flash("Lista de productos")
    return render_template('productos.html', l_productos = lista_productos, titulo='Lista de productos')

@app.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method=='GET':
        form=Producto()
        return render_template('nuevo.html', form=form, titulo='Registro de nuevo producto')
    elif request.method=='POST':
        code=request.form['codigo']
        nombre=request.form['nombre']
        precio=request.form['precio']
        cantidad=request.form['cantidad']
        bd.sql_insert_product(code,nombre,precio,cantidad)
        flash(f'producto {nombre} registrado con exito!')
        return render_template('base.html', titulo='registro de nuevo producto')
@app.route('/edit', methods=['GET'])
def editarProduct():
    code = request.args.get("codigo")
    cantidad = request.args.get("cantidad")
    bd.sql_edit_product(code,cantidad)
    flash(f'Producto {code} actualizado con exito')
    return render_template('base.html')

@app.route('/delete', methods=['GET'])
def eliminarProduct():
    code = request.args.get("codigo")
    bd.sql_delete_producto(code)
    flash(f'Producto {code} eliminado con exito')
    return render_template('base.html')


#app.run(port=5000, debug=True)
app.run(host='localhost', port=443, ssl_context=('micertificado.pem','llaveprivada.pem'))