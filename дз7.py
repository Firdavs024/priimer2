# ocenki_za_chetvert={'Маша':5,'Саша':5,'Олег':4,'Паша':3,'Федя':3,'Маша':2}
# for k,v in ocenki_za_chetvert.items():
#     print(f'{k}-{v}')
# while True:
#     action=input('Изменить оценку?  ')
#     if action=='да':
#         choise_name=input('Имя ученика:  ')
#         new_point=int(input('Новая оценка:  '))
#         ocenki_za_chetvert[choise_name]=new_point
#         for k, v in ocenki_za_chetvert.items():
#             print(f'{k}-{v}')

ocenki_chetverti={'Миша':{'История':2,'Математика':5,'Гоеграфия':5,'Физика':5,'Химия':5},
      'Саша':{'История':5,'Математика':5,'География':5,'Физика':5,'Химия':5},
      'Паша':{'История':5,'Математика':5,'География':5,'Физика':5,'Химия':5}}
for k,v in ocenki_chetverti.items():
    print(f'{k}-{v}')
while True:
    action=input('Что хотите сделать:\n'
                 '1-Изменить оценки\n'
                 '2-Просмотр оценок')
    if action=='1':
        name=input('Выбрать ученика')
        predmet=input('Выбрать предмет')
        point=int(input('Оценка'))
        ocenki_chetverti[name][predmet]=point
        for k, v in ocenki_chetverti.items():
            print(f'{k}-{v}')
    if action=='2':
        for k, v in ocenki_chetverti.items():
            print(f'{k}-{v}')
    if action=='3':
          name=input('Имя нового ученика ')
          predmet=input('Предмет ')
          point=int(input('Оценка'))
          ocenki_chetverti[name]=predmet,point
          for k, v in ocenki_chetverti.items():
              print(f'{k}-{v}')