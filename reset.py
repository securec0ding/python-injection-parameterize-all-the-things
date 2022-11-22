from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  phone = db.Column(db.String(12))
  dob = db.Column(db.String(10))
  salary = db.Column(db.Numeric(10,2))

  def __init__(self, name, email, phone, dob, salary):
    self.name = name
    self.email = email
    self.phone = phone
    self.dob = dob
    self.salary = salary

  def __repr__(self):
    return '<Employee %r>' % self.name

db.drop_all()
db.create_all()

employees = [Employee(
  'Alice',
  'alice@bigco.rp',
  '202-555-5555',
  '04-01-1956',
  '75000.00'
),
Employee(
  'Bob',
  'bob@bigco.rp',
  '323-867-5309',
  '12-31-1984',
  '40000.00'
)]

for employee in employees:
  db.session.add(employee)
db.session.commit()