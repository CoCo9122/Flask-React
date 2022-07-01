from flask import Blueprint, jsonify
from models.exsample1 import Exsample1Model

exsample1_bp = Blueprint('exsample', __name__)

@exsample1_bp.route('/')
def index():
    return 'exsample1'
    

@exsample1_bp.route('/data')
def fetchData():
    records = Exsample1Model.query.all()
    return jsonify([record.to_dict() for record in records])

@exsample1_bp.route('/test')
def test():
    return 'exsample1test'