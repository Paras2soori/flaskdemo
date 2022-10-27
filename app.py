
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgress:admin@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(200),nullable = False)

    
        


@app.route('/')
def index():
    
    return 'hello world'



if __name__== '__main__':
    app.run(debug=True)