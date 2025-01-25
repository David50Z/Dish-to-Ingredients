 
 

import { AddForm } from "./AddForm.js";
import { AddIngredient } from "./AddIngredient.js";
 console.log("s")
 const addIngredientBtn = document.getElementById('addIngredientBtn');

 addIngredientBtn.addEventListener('click', () => {
    AddForm()
 });
     

 document.getElementById('add-ingredient').addEventListener('click', async function (event) {
    AddIngredient(event)
 });