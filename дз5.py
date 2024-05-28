all_products={'весь склад':{'картошка':20,'помидор':30,'лук':25}}
korzina={}
while True:
    choice = input('Хотите добавить или посмотреть весь список?')
    if choice.lower()== 'добавить':
        products=input('продукт:')
        count=int(input('кол-во'))
        all_products['весь склад'][products]=count
    elif choice.lower()=='продукт':
        print(all_products)
        my_korzina = input('что нибудь добваить в корзину?')
        count_korzina = int(input('количество'))
        all_products['весь склад'][my_korzina] -= count_korzina
        korzina[my_korzina]=count_korzina
        print(korzina)
        print(all_products)
        end=input('Закончить покупку?')
        if end=='yes':
            break
        elif end == 'заменить':
            korzina.clear()
            zamena=input('Какой товар выберите?')
            count_zamena=int(input('кол-во'))
            all_products['весь склад'][zamena] -= count_zamena
            korzina[zamena]=count_zamena
            print(korzina)
            print(all_products)
        end2=input('закончить покупку?')
        if end2=='yes':
            break
        elif end2=='стереть':
            korzina.clear()
            print(korzina)
            break