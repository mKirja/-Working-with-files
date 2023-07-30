cook_book = {}

with open('cook_book.txt','r',encoding='utf-8') as f:    
    #print(f.read())
    for line in f:
        dish_name = line.strip() #название блюда
        quantity_of_ingredients = int(f.readline()) #кол-во ингредиентов
        ingredients_list = [] #список ингредиентов
        for quantity in range(quantity_of_ingredients):
            i = f.readline()
            ingredient_name, quantity, measure  = i.strip().split(' | ')
            ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dish = {dish_name: ingredients_list}
            #print(ingredients_list)
        blank_line = f.readline()
        cook_book.update(dish)
print(f'cook_book = {cook_book}')