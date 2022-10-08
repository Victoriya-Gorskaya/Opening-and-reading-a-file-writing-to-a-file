dishes = {}

with open('recipes.txt', 'rt', encoding = 'utf8') as file:
    for dish in file:
        dish_name = dish.strip()
        recipes = {dish_name: []}
        quantity_of_ingredients = file.readline()
        for portions in range(int(quantity_of_ingredients)):
            products = file.readline()
            ingredient_name, quantity, measure = products.strip().split(' | ')
            recipes[dish_name].append({'ingredient_name' : ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})
        blank_line = file.readline()
        dishes.update(recipes)

print(f"cook_book = {dishes}")