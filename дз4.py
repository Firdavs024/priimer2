# name=('pasha')
# n=[a.upper() for a in name]
# print(n)

# name=['Oleg','Kotov']
# se=['Est','Yabloko']
# n=[i[0] for i in name]
# s=[i[0] for i in se]
# print(n,s)
#
# kvadrat=[2,3,4,5,6,7]
# umnoj=[i*i for i in kvadrat]
# print(umnoj)
#
# import random
# ch=[random.randint(10,40)for i in range(5)]
# print(ch)

r=input('какое число хотите видеть в квадрате: ')
f=[int(i)+int(i) for i in r]
print(f)

# s=input('')
# a=[int(i)*3 for i in s if int(s)>=0]
# print(a)
#
# s=['aleksandra','grigoruy','daria','oksana','zlata']
# v=[i[0::2]for i in s]
# print(v)
