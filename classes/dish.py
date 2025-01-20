from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dish(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.JSON, nullable=False)

    def __init__(self, name, ingredients):
        """
        Initialize a Dish object.

        :param dish_id: (int) Unique identifier for the dish
        :param name: (str) Name of the dish
        :param ingredients: (list of dicts) List of ingredients with their quantities
        """
        self.name = name
        self.ingredients = ingredients  # List of {"ingredient": str, "quantity": str}

    def __repr__(self):
        """
        Provide a string representation of the Dish object for debugging.
        """
        return f"Dish(id={self.id}, name={self.name}, ingredients={self.ingredients})"

    def add_ingredient(self, ingredient, quantity):
        """
        Add an ingredient to the dish.

        :param ingredient: (str) Name of the ingredient
        :param quantity: (str) Quantity of the ingredient
        """
        self.ingredients.append({"ingredient": ingredient, "quantity": quantity})

    def to_dict(self):
        """
        Convert the Dish object into a dictionary for serialization.

        :return: (dict) Representation of the dish
        """
        try:
            return {
                "id": self.id,
                "name": self.name,
                "ingredients": self.ingredients,
            }
        except Exception as e:
            print(f"error in to_dict: {e}")


    #_id = db.Column("id", db.integer, primary_key=True)
    #name = db.Column( db.String(100))
    #ingredients = db.Column(db.Array)
    #quantity = db.Column()
    
    #def __init__(self, name, email):
    #    self.name = name
    #    self.email = email