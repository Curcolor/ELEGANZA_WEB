from app import db

class Rol(db.Model):
    __tablename__ = 'roles'
    
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_de_rol = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre_de_rol):
        self.nombre_de_rol = nombre_de_rol

    def __repr__(self):
        return f'<Rol {self.nombre_de_rol}>' 