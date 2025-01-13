export async function AddIngredient(event) {
    event.preventDefault();
     let dishName = document.getElementById('dish_name')
     console.log(dishName.value)
     if (dishName.value.length < 1) {
   throw error
     }
     let ingredientList = []
     let ingredientsDiv = document.getElementById('ingredients-container');
     let items = ingredientsDiv.children
     for (let i = 0; i < items.length; i++) {
        ingredientList.push({
                Ingredient: items[i].children[0].value,
                Quantity: items[i].children[1].value
            })
        }
     
     let result = {
        dish: dishName.value,
        ingredients: ingredientList
        }
     
     const response = await fetch('http://127.0.0.1:5000/add-dish', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(result),
        });
            
   window.location = 'http://127.0.0.1:5000/dishes';
}