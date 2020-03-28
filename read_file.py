cook_book = {}
list = []
with open("recipes.txt") as f:
  while True:
    try:
        name_bluda = f.readline().strip()
        kol_vo = f.readline().strip()
        #print(name_bluda, kol_vo)
        list = []
        for number in range(int(kol_vo)):
          ingredient_name = f.readline().strip().split("|")
          #print(ingredient_name)
          #print(ingredient_name[0])
          list.append({'ingredient_name': ingredient_name[0].strip(), 'quantity': ingredient_name[1].strip(), 'measure': ingredient_name[2].strip()})
       
        cook_book[name_bluda] =  list
        f.readline()
        if not name_bluda:
          break
    except:
      #print("Jib,rf")
      break

for jjj1, jjj in cook_book.items():
    print(jjj1, jjj)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book1 = {}

    kol_vo_blud = len(dishes)
    #print(len(dishes))
    for number in range(kol_vo_blud):
      for key, cook_book11 in cook_book.items():
          if key == dishes[number]:
              kol_vo1 = len(cook_book11)
              #print(kol_vo1)
              for numer1 in range(kol_vo1):
                list = []
                #print(cook_book1[cook_book11[numer1]['ingredient_name']])#
                ggg = cook_book11[numer1]['ingredient_name']
                ggg1 = cook_book1.get(ggg)
                if ggg1 == None:
                  list.append({'measure': cook_book11[numer1]['measure'], 'quantity':int(cook_book11[numer1]['quantity'])*person_count})
                  cook_book1[cook_book11[numer1]['ingredient_name']] = list
                  #print(list)
                #cook_book1["measure"] =cook_book11[numer1]['measure']
                else:
                  #cook_book1[cook_book11[numer1]['ingredient_name']["quantity"]] = 1
                  print('Такой ключ есть, не могу сообразить как увеличить количество quantity')
   
    for jjj1, jjj in cook_book1.items():
      print(jjj1,jjj)
           
  

  
print("====================================")
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)