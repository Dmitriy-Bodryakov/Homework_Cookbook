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
