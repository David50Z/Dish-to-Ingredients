from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

dishes = []

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/add-dish", methods=["POST"])
def add_dish():
    data = request.get_json()
    dish = data.get('dish')
    ingredients = data.get('ingredients')
    dishes.append(data)

    return jsonify(dishes), 201

@app.route("/dishes")
def get_dishes():
    return jsonify(dishes)
    

@app.route("/")
def form():
    return render_template('form.html')

def home():
    return "Home"

if (__name__) == "__main__":
    app.run(debug=True)