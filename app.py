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


@app.route('/', methods=['GET', 'POST'])
def employees():
  name = request.form.get('search', '')
  with db.engine.connect() as conn:
    results = conn.execute("SELECT * FROM Employee WHERE name LIKE '%" + name + "%'").fetchall()
  return render_template('employees.html', employees=results)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)