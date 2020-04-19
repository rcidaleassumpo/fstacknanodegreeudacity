from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


db = SQLAlchemy(app)

# Reminder,
# classes map to Tables
# attributes map to columns
# by defining the class, SQL and setting that class inheriting from db.Model, it will then pick up
# and create the table whe we call db.createAll
class Person(db.Model):

    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

class SomeClass(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Setting unique to true is good when you don't want to repeat the same.
    name = db.Column(db.String(), nullable=False)

class Family(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Setting unique to true is good when you don't want to repeat the same.
    name = db.Column(db.String(), nullable=False, unique=True)

db.create_all()


db.session.bulk_insert_mappings(SomeClass,
    [dict(name='Gatinha'), dict(name='Ruivinha')]
)

db.session.add(Person(name='Renan'))
db.session.add(SomeClass(name='Thiago'))
db.session.add(SomeClass(name='Pamela'))
db.session.add(SomeClass(name='Christine'))
db.session.add(SomeClass(name='Gianna'))
db.session.add(SomeClass(name='Jairo'))
db.session.commit()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
    app.run()



