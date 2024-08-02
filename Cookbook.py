from pprint import pprint
import os

p = os.path.abspath('recipes.txt')
print(p)
Cook_book = {}
with open('c:/Users/bodri/OneDrive/Рабочий стол/Homework_Cookbook/recipes.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dish = line.strip()
        Cook_book[dish] = []
        ingredients_quantity = int(f.readline().strip())
        for item in range(ingredients_quantity):
            ingredients = {}
            ingredient = f.readline().strip().split(' | ')
            ingredients['ingredient_name'] = ingredient[0]
            ingredients['quantity'] = int(ingredient[1])
            ingredients['measure'] = ingredient[2]
            Cook_book[dish].append(ingredients)
        f.readline()
pprint(Cook_book)    

def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for food in dishes:
        if food in Cook_book.keys():
            for ingredient in Cook_book[food]: 
                if ingredient['ingredient_name'] not in ingredients_list:
                    ingredients_list[ingredient['ingredient_name']] = { 'measure' : ingredient['measure'], 'quantity' : (person_count * ingredient['quantity']) }
                else:
                    ingredients_list[ingredient['ingredient_name']]['quantity'] += person_count * ingredient['quantity']
    return ingredients_list
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))