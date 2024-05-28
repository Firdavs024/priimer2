class Player:
    def __init__(self,speed,stamina):
        self.speed=speed
        self.stamina=stamina
s=[]
class goalkeeper(Player):
    def __init__(self,speed,stamina,jump_height):
        self.jump_height=jump_height
        s.append(speed)
        s.append(stamina)
        s.append(jump_height)
objekt=Player('35 km/ч','100')
objekt1=goalkeeper(speed='30 km/ч',stamina='80',jump_height='3 metr')
print(f'Player {vars(objekt)}')
print (f'Goalkeeper {s}')