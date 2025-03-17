from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.category}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        desc = request.form['desc']
        amount = request.form['amount']
        exp = Expense(category=category, amount=amount, desc=desc, date=date)
        db.session.add(exp)
        db.session.commit()

    allexp = Expense.query.all()
    
    # List all images in static folder
    images = [f for f in os.listdir("static") if f.endswith((".png", ".jpg", ".jpeg"))]

    return render_template('index.html', allexp=allexp, images=images)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    exp = Expense.query.get(sno)
    if request.method == 'POST':
        exp.date = request.form['date']
        exp.category = request.form['category']
        exp.amount = request.form['amount']
        exp.desc = request.form['desc']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update.html', exp=exp)

@app.route('/delete/<int:sno>')
def delete(sno):
    exp = Expense.query.get(sno)
    db.session.delete(exp)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
