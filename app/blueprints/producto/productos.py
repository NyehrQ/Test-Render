from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.productos_service import ProductoService  # Debes crear este servicio
import json 

producto_bp = Blueprint('producto', __name__)

@producto_bp.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']

        productos = ProductoService.obtener_productos()  # Debes crear este método
        nuevo_producto = {
            "id": str(len(productos) + 1),  
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }

        try:
            if ProductoService.agregar_producto(nuevo_producto):
                flash("Producto agregado exitosamente.", "success")
                return redirect(url_for('producto.ver_productos')) 
            else:
                flash("Error al agregar el producto.", "danger")
        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "danger")

    return render_template('producto/agregar_producto.html')

@producto_bp.route('/editar_producto/<id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    producto_a_editar = ProductoService.obtener_producto_por_id(id_producto)  # Obtén el producto por ID

    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']

        # Crear un diccionario para el producto actualizado
        producto_actualizado = {
            "id": id_producto,
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        }

        try:
            if ProductoService.actualizar_producto(producto_actualizado):
                flash("Producto actualizado exitosamente.", "success")
                return redirect(url_for('producto.ver_productos')) 
            else:
                flash("Error al actualizar el producto.", "danger")
        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "danger")

    return render_template('producto/editar_producto.html', producto=producto_a_editar)


@producto_bp.route('/eliminar_producto/<id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    try:
        if ProductoService.eliminar_producto(id_producto):
            flash("Producto eliminado exitosamente.", "success")
        else:
            flash("Error al eliminar el producto.", "danger")
    except Exception as e:
        flash(f"Ocurrió un error: {str(e)}", "danger")

    return redirect(url_for('producto.ver_productos'))


@producto_bp.route('/ver_productos', methods=['GET'])
def ver_productos():
    productos = ProductoService.obtener_productos()  # Debes crear este método
    return render_template('producto/ver_productos.html', productos=productos)
