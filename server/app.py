#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakery = Bakery.query.all()
    
    return [b.to_dict() for b in bakery]

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id = id).first()
    response = make_response(
        bakery.to_dict(),200
    )
    return response
@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    bakery = BakedGood.query.order_by(desc(BakedGood.price)).all()
    

    return [b.to_dict() for b in bakery]

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    bakery = BakedGood.query.order_by(desc(BakedGood.price)).first()

    return bakery.to_dict()
if __name__ == '__main__':
    app.run(port=5555, debug=True)
