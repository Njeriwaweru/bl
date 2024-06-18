from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///categories.db'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    icon = db.Column(db.String(200), nullable=True)

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = Category.query.distinct(Category.name).all()
    return jsonify([{'id': cat.id, 'name': cat.name, 'icon': cat.icon} for cat in categories])

# Debug route to query database and retrieve categories
@app.route('/api/categories/debug', methods=['GET'])
def debug_categories():
    categories = Category.query.all()
    category_list = [{'id': cat.id, 'name': cat.name, 'icon': cat.icon} for cat in categories]
    return jsonify(category_list)

if __name__ == '__main__':
    app.run(debug=True)
