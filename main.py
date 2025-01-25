from flask import Flask, render_template, request, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from classes.dish import Dish, db
from python_hooks.getAll import getAll
app = Flask(__name__)
print(getAll)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dishes.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)


db.init_app(app)

dishes = []

@app.route("/add-dish", methods=["POST"])
def add_dish():
    data = request.get_json()
    '''dish = data.get('dish')
    ingredients = data.get('ingredients')
    dishes.append(data)'''
    print(data)
    new_dish = Dish(name=data['dish'], ingredients=data['ingredients'])
    with app.app_context():
        db.session.add(new_dish)
        db.session.commit()

    return jsonify(dishes), 201

@app.route("/dishes")
def get_dishes():
    return getAll(Dish.query.all())
    

@app.route("/")
def form():
    result = []
    every_dish = Dish.query.all()
    i = 0
    for dish in every_dish:
        current_dish = {
            'name': dish.name,
            'ingredients': dish.ingredients
        }
        result.append(current_dish)
        i = i + 1 
        if dish.id == 2:
            
            with app.app_context():
                db.session.commit()
    print(result)
    
    return render_template('form.html')


def home():
    return "Home"

if (__name__) == "__main__":
    with app.app_context():  
        db.create_all()  

        
    app.run(debug=True)