from app import db

class TipoProveedor(db.Model):
    __tablename__ = 'tipo_proveedor'
    
    id_tipo_proveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f'<TipoProveedor {self.nombre}>' 