from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Запуск приложения...")

    with app.app_context():
        db.create_all()  
        logging.info("База данных инициализирована.")

    logging.info("Запуск сервера Flask на порту 5000...")
    app.run(debug=True, host='0.0.0.0', port=5000)
