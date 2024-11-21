from app import db

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    
    id_proveedor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_tipo_proveedor = db.Column(db.Integer, db.ForeignKey('tipo_proveedor.id_tipo_proveedor'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.Text, nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.Boolean, default=True, nullable=True)

    def __init__(self, nombre, id_tipo_proveedor, direccion=None, telefono=None, email=None, estado=True):
        self.nombre = nombre
        self.id_tipo_proveedor = id_tipo_proveedor
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.estado = estado

    def __repr__(self):
        return f'<Proveedor {self.nombre}>' 