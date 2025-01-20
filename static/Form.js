 
 
// Reference the ingredients container and the add button
import { AddForm } from "./AddForm.js";
import { AddIngredient } from "./AddIngredient.js";
 console.log("s")
 const addIngredientBtn = document.getElementById('addIngredientBtn');
     
 // Add a new ingredient and quantity input group
 addIngredientBtn.addEventListener('click', () => {
    AddForm()
 });
     
 // Handle form submission
 document.getElementById('add-ingredient').addEventListener('click', async function (event) {
    AddIngredient(event)
 });