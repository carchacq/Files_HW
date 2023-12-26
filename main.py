# Задание 1
cook_book = {}
with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    for line in recipes:
        dish = line.strip()
        prod_count = int(recipes.readline())
        ingr_list = []
        for i in range(prod_count):
            ingredient_name, quantity, measure = recipes.readline().strip().split('|')
            ingr_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, "measure": measure})
        cook_book[dish] = ingr_list
        recipes.readline()
# print(cook_book)

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in shopping_list.keys():
                    shopping_list.update({ingr['ingredient_name']: {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}})
                else:
                    shopping_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count
    return shopping_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))






# Задание 3
import os

filename1 = '1.txt'
filename2 = '2.txt'
filename3 = '3.txt'
filename4 = '4.txt'
file_path1 = os.path.join(os.getcwd(), 'sorted', filename1)
file_path2 = os.path.join(os.getcwd(), 'sorted', filename2)
file_path3 = os.path.join(os.getcwd(), 'sorted', filename3)
file_path4 = os.path.join(os.getcwd(), 'sorted', filename4)

file1 = open(file_path1, 'r', encoding='utf-8')
file2 = open(file_path2, 'r', encoding='utf-8')
file3 = open(file_path3, 'r', encoding='utf-8')
file4 = open(file_path4, 'a', encoding='utf-8')
dict_files = {file1: filename1, file2: filename2, file3: filename3}
dict = {}
file_list = [file1, file2, file3]
counter = 0

for file in file_list:
    text = file.read()
    if text.count('\n') > 1:
        counter = text.count('\n') + 1
    else:
        counter = text.count('\n')
    # counter = len(leng)
    dict.update({dict_files[file]: [counter, text]})

dict = sorted(dict.items(), key=lambda item: item[1])

for i in dict:
    file4.write(str(i[0]))
    file4.write('\n')
    file4.write(str(i[1][0]))
    file4.write('\n')
    file4.write(str(i[1][1]))
    file4.write('\n\n')

for file in file_list:
    file.close()