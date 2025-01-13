export function AddForm() {
    const ingredientsContainer = document.getElementById('ingredients-container');
    const newGroup = document.createElement('div');
    newGroup.classList.add('ingredient-group');

    const ingredientInput = document.createElement('input');
    ingredientInput.type = 'text';
    ingredientInput.placeholder = 'Ingredient';
    ingredientInput.required = true;

    const quantityInput = document.createElement('input');
    quantityInput.type = 'text';
    quantityInput.placeholder = 'Quantity';
    quantityInput.required = true;

    newGroup.appendChild(ingredientInput);
    newGroup.appendChild(quantityInput);
    ingredientsContainer.appendChild(newGroup);
}