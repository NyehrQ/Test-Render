from flask import Flask, redirect, url_for
from app.blueprints.autenticacion.rutas import autenticacion_bp
from app.blueprints.dashboard.rutas import dashboard_bp
from app.blueprints.usuario.rutas import usuario_bp
from app.blueprints.producto.rutas import producto_bp
from app.blueprints.inicio.rutas import inicio_bp
from app.blueprints.venta.rutas import ventas_bp

def create_app():
    app = Flask(__name__)

    
    app.config['SECRET_KEY'] = '$2a$10$l3Zw/L9LWrrPSNpWfQCTCODDGB2PsYk3/D.GYyqtAfRrh.WZKmP.W'

    app.register_blueprint(autenticacion_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(inicio_bp)
    app.register_blueprint(ventas_bp)
    
    return app
