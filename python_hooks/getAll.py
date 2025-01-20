def getAll(data):
    result = []
    every_dish = data
    i = 0
    for dish in every_dish:
        current_dish = {
            'name': dish.name,
            'ingredients': dish.ingredients
        }
        result.append(current_dish)
        i = i + 1 
        #print(dish)
    return result