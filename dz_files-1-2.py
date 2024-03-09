import pprint
cook_book = {}
def add_ingrid(ingrid):
    line=ingrid.strip('\n').split(' | ')
    ingredient_name = line[0]
    quantity = line[1]
    measure = line[2]
    return {'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure}
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingrid in cook_book[dish]:
            if ingrid['ingredient_name'] in result:
                result[ingrid['ingredient_name']].update(
                    [
                        ('quantity', (result[ingrid['ingredient_name']]['quantity'] + int(ingrid['quantity'])*person_count))
                    ]
                )
            else:
                result[ingrid['ingredient_name']] = {'measure' : ingrid['measure'], 'quantity' : int(ingrid['quantity'])*person_count}
    return result
with open('files/recipes.txt', encoding='utf-8' ) as f:
    name = f.readline().strip()
    while name != '':
        kol_ingrid = f.readline().strip()
        spisok = []
        for i in range(int(kol_ingrid)):
            if i == 0:
                spisok = [add_ingrid(f.readline())]
            else:
                spisok.append(add_ingrid(f.readline()))
        cook_book[name] = spisok
        f.readline().strip()
        name = f.readline().strip()

#pprint.pprint(cook_book)

#pprint.pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))