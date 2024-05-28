         ####CLASS STUDENT####


# class Student1:
#     def __init__(self,name1='Ivan',age='18',group_number='10A'):
#         self.name1=name1
#         self.age=age
#         self.group=group_number
#     def change_name(self, new_name,new_age):
#         self.name1=new_name
#         self.age=new_age
#     def change_group(self,new_group):
#         self.group=new_group
# class Student2:
#     def __init__(self,name2='Olya',age='18',group_number='10B'):
#         self.name2=name2
#         self.age=age
#         self.group=group_number
#     def change_name(self, new_name,new_age):
#         self.name2=new_name
#         self.age=new_age
#     def change_group(self,new_group):
#         self.group=new_group
# class Student3:
#     def __init__(self,name3='Oleg',age='18',group_number='10C'):
#         self.name3=name3
#         self.age=age
#         self.group=group_number
#     def change_name(self, new_name,new_age):
#         self.name3=new_name
#         self.age=new_age
#     def change_group(self,new_group):
#         self.group=new_group
# class Student4:
#     def __init__(self,name4='Jack',age='18',group_number='10D'):
#         self.name4=name4
#         self.age=age
#         self.group=group_number
#     def change_name(self, new_name,new_age):
#         self.name4=new_name
#         self.age=new_age
#     def change_group(self,new_group):
#         self.group=new_group
# class Student5:
#     def __init__(self,name5='Max',age='18',group_number='10E'):
#         self.name5=name5
#         self.age=age
#         self.group=group_number
#     def change_name(self, new_name,new_age):
#         self.name5=new_name
#         self.age=new_age
#     def change_group(self,new_group):
#         self.group=new_group
# objekt=Student1()
# objekt2=Student2()
# objekt3=Student3()
# objekt4=Student4()
# objekt5=Student5()
# # #
# while True:
#
#     print(f'Имя {objekt.name1}',f'{objekt.age} лет',f'Группа {objekt.group}','\n',
#           f'Имя {objekt2.name2}',f'{objekt2.age} лет',f'Группа {objekt2.group}','\n',
#           f'Имя {objekt3.name3}',f'{objekt3.age} лет',f'Группа {objekt3.group}','\n',
#           f'Имя {objekt4.name4}',f'{objekt4.age} лет',f'Группа {objekt4.group}','\n',
#           f'Имя {objekt4.name4}',f'{objekt4.age} лет',f'Группа {objekt4.group}','\n',)
#     action=input('Изменить данные студента под номером:  ')
#     if action=='1':
#         action=input('Что хотите изменить:  ')
#         if action=='имя':
#             new_name=input('Новое имя:  ')
#             new_age=input('Новый возраст:  ')
#             objekt.change_name(new_name, new_age)
#         if action=='группу':
#             new_group=input('Новая группа')
#             objekt.change_group(new_group)
#     if action == '2':
#         action = input('Что хотите изменить:  ')
#         if action == 'имя':
#             new_name = input('Новое имя:  ')
#             new_age = input('Новый возраст:  ')
#             objekt2.change_name(new_name, new_age)
#         if action == 'группу':
#             new_group = input('Новая группа')
#             objekt2.change_group(new_group)
#     if action == '3':
#         action = input('Что хотите изменить:  ')
#         if action == 'имя':
#             new_name = input('Новое имя:  ')
#             new_age = input('Новый возраст:  ')
#             objekt3.change_name(new_name, new_age)
#         if action == 'группу':
#             new_group = input('Новая группа')
#             objekt3.change_group(new_group)
#     if action == '4':
#         action = input('Что хотите изменить:  ')
#         if action == 'имя':
#             new_name = input('Новое имя:  ')
#             new_age = input('Новый возраст:  ')
#             objekt4.change_name(new_name, new_age)
#         if action == 'группу':
#             new_group = input('Новая группа')
#             objekt4.change_group(new_group)
#     if action == '5':
#         action = input('Что хотите изменить:  ')
#         if action == 'имя':
#             new_name = input('Новое имя:  ')
#             new_age = input('Новый возраст:  ')
#             objekt5.change_name(new_name, new_age)
#         if action == 'группу':
#             new_group = input('Новая группа')
#             objekt5.change_group(new_group)


    ####CLASS MATH####

# class Math:
#     def addition(self,a,b):
#         self.multiplication=a*b
#         self.umnoj=a+b
#         self.division=a//b
#         self.subtraction=a-b
#
# otvet=Math()
# otvet.addition(6,3)
# print(f'Ваш ответ {otvet.umnoj} {otvet.multiplication} {otvet.division} {otvet.subtraction}')


   ####CLASS CAR####

class Car:
    def __init__(self,color,type,year):
        self.color=color
        self.type=type
        self.year=year
    def start(self):
        print(f'Автомобиль заведен')
    def stop(self):
        print(f'Автомообиль заглушен')
Car1=Car('Черный','BMW','2023')
Car1.start()
Car1.stop()
print(f'Цвет {Car1.color}',f'Модель {Car1.type}',f'Год выпуска {Car1.year}')