imena=['oleg','alex','olya']
nomber=['77777','88888']
menu=input('Что хоите сделать? 1-добваить 2-удалить 3-изменить 4-просмотр контаков')
while True:
    if menu == '1':
         new_name=input('Введите имя контакта')
         if new_name in imena:
             print('это имя уже существует')
         else:
             new_nomber=input('Введите номпер контакта')
             if new_nomber in nomber:
                 print('номер уже есть')
             else:
                 imena.append(new_name)
                 nomber.append(new_nomber)
    elif menu == '2':
         delet_name=input('Введите имя которое нужно удалить')
         delet_nomber=input('Введите номер который нужно удалить')
         imena.remove(delet_name)
         nomber.remove(delet_nomber)
    elif menu == '3':
        change_name=input('Какое имя контакта хотели бы изменить (ИНДЕКС КОНТАКТА)')
        if change_name not in imena:
            print('error')
        index_name=imena.index(change_name)
        new_name=input('на какое имя')
        imena[index_name]=new_name
        # if change_name== '0':
        #     new_index=input('Новое название')
        #     imena[0]=new_index
        # if change_name == '1':
        #     new_index = input('Новое название')
        #     imena[1] = new_index
        change_nomber =input('Какой номер контакта хотели бы изменить (ИНДЕКС КОНТАКТА)')
        if change_nomber not in nomber:
            print('error')
        index_nomber=nomber.index(change_nomber)
        new_nomber=input('на какой номер')
        nomber[index_nomber]=new_nomber
        # if change_nomber=='0':
        #     new_index1=input('Новый номер')
        #     nomber[0]=new_index1
        # if change_nomber=='1':
        #     new_index1=input('Новый номер')
        #     nomber[1]=new_index1

    elif menu == '4':
         print(imena,nomber)
    if menu == '4':
        break

    print(imena,nomber)