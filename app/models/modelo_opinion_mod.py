from app import db
from datetime import datetime, UTC

class OpinionMod(db.Model):
    __tablename__ = 'opiniones_mod'
    
    id_opinion_mod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_opinion = db.Column(db.Integer, db.ForeignKey('opiniones.id_opinion'), nullable=False)
    id_moderador = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'), nullable=False)
    accion = db.Column(db.String(50), nullable=False)
    motivo = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)

    def __init__(self, id_opinion, id_moderador, accion, motivo=None):
        self.id_opinion = id_opinion
        self.id_moderador = id_moderador
        self.accion = accion
        self.motivo = motivo

    def __repr__(self):
        return f'<OpinionMod {self.id_opinion_mod}>' 