with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        num_ingredients = int(file.readline().strip())
        ingredients = []
        for _ in range(num_ingredients):
            ingredient_info = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_info[0],
                'quantity': int(ingredient_info[1]), 
                'measure': ingredient_info[2]
            })
        cook_book[dish] = ingredients
        file.readline()

for dish, ingredients in cook_book.items():
    print(f"{dish}:")
    for ingredient in ingredients:
        print(f"  {ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}")
    print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")
    
    return shop_list

# Пример использования
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
result = get_shop_list_by_dishes(dishes, person_count)
for ingredient, details in result.items():
    print(f"{ingredient} | {details['quantity']} | {details['measure']}")
