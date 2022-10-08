dishes_dict = {}

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
        dishes_dict.update(recipes)

# print(f"cook_book = {dishes_dict}")

def get_shop_list_by_dishes(dishes: list, person_count):
    shop_list = {}
    for d in dishes:
        for dish, ingredients in dishes_dict.items():
            if d == dish:
                for position in ingredients:
                    ingredient_name = position['ingredient_name']
                    measure = position['measure']
                    shop_l = {ingredient_name : {}}
                    quantity = int(position['quantity'])
                    if ingredient_name in shop_list:
                        quantity += int(position['quantity'])
                        shop_l[ingredient_name] = {'measure': measure, 'quantity': quantity * person_count}
                    else:
                        shop_l[ingredient_name] = {'measure': measure, 'quantity': quantity * person_count} 
                    shop_list.update(shop_l)
    return shop_list

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 10)