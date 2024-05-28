# baza={'Занятые номера':{'Паша':1,'Саша':2},'Свободные номера':{3:'свободно',4:'свободно',5:'свободно'
#                                                                ,6:'свободно',7:'свободно',8:'свободно'}}
# while True:
#     action=input('действие ')
#     if action=='добавить':
#         print(baza)
#         new_klient=input('Имя нового клиента')
#         new_nomber=int(input('в какой номер '))
#         baza['Занятые номера'][new_klient]=new_nomber
#         del baza['Свободные номера'][new_nomber]
#         print(baza)
#     if action=='удалить':
#         name_delet = input('Нас покаинул: ')
#         nomber_creat= int(input('номер'))
#         del baza['Занятые номера'][name_delet]
#         baza['Свободные номера'][nomber_creat]='свободно'
#         print(baza)
#     if action=='просмотр комнат':
#         for k,v in baza.items():
#             print (f'{k}:{v}')





