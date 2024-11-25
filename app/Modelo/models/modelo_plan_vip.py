from app import db

class PlanVip(db.Model):
    __tablename__ = 'planes_vip'
    
    id_plan = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Decimal(10,2), nullable=False)
    duracion_meses = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=True)

    def __init__(self, nombre, precio, duracion_meses, descripcion=None, estado=True):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.duracion_meses = duracion_meses
        self.estado = estado

    def __repr__(self):
        return f'<PlanVip {self.nombre}>' 