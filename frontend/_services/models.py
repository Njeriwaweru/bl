from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BusinessList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    contact_person = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    about = db.Column(db.String(200), nullable=False)
    images = db.Column(db.String(500), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    bookings = db.Column(db.String(500), nullable=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
