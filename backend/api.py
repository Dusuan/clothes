from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:psicocarlosclothes@clothes/postgres'
db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"
    
    def __init__(self, description):
         self.description = description


@app.route('/')
def mensaje():
    return 'Hola!!!'

if __name__ == '__main__':
    app.run(debug=True)


    

    """For some reason i cant run db.create_all() in shell """