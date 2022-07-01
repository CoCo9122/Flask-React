from database import db

class Exsample1Model(db.Model):
    __tablename__ = 'exsample1'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)

    def __init__(self, name=None, state=None):
        self.name = name
        self.state = state

    def __repr__(self):
        return '<Exsample1 {}:{}>'.format(self.id, self.name)
    
    def to_dict(self, ):
        return {
            'id': self.id,
            'name': self.name,
            'state':self.state
        }