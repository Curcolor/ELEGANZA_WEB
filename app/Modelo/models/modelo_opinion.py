from app import db
from datetime import datetime, UTC

class Opinion(db.Model):
    __tablename__ = 'opiniones'
    
    id_opinion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=True)

    def __init__(self, id_usuario, id_producto, calificacion, comentario=None, estado=True):
        self.id_usuario = id_usuario
        self.id_producto = id_producto
        self.calificacion = calificacion
        self.comentario = comentario
        self.estado = estado

    def __repr__(self):
        return f'<Opinion {self.id_opinion}>' 