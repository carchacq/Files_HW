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

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))








# Задание 3
# import os
# file_path1 = os.path.join(os.getcwd(), 'sorted', '1.txt')
# file_path2 = os.path.join(os.getcwd(), 'sorted', '2.txt')
# file_path3 = os.path.join(os.getcwd(), 'sorted', '3.txt')
# file_path4 = os.path.join(os.getcwd(), 'sorted', '4.txt')
#
# dict = {}
# one_txt = open(file_path1, 'r', encoding='utf-8')
# one_lines = one_txt.readlines()
#
# two_txt = open(file_path2, 'r', encoding='utf-8')
# two_lines = two_txt.readlines()
#
# three_txt = open(file_path3, 'r', encoding='utf-8')
# three_lines = three_txt.readlines()
#
# dict = {one_txt: one_lines, two_txt: two_lines, three_txt: three_lines}
# sorted_lines = [one_lines, two_lines, three_lines]
# sorted_lines.sort(key=len)
#
#
# with open(file_path4, 'a', encoding='utf-8') as all_txt:
#     for i in sorted_lines:
#         if i in dict.values():
#             a = ''.join(i)
#             all_txt.write(a)
#             all_txt.write('\n')
# # print(sorted_lines)