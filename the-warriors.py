class Warrior:
    health = 50
    attack = 5
    is_alive = True
    
class Knight(Warrior):
    attack = 7

    
def fight(unit_1, unit_2):
    result = True
    while unit_1.is_alive == True or unit_2.is_alive == True:
        unit_2.health = unit_2.health - unit_1.attack
        if unit_2.health < 0:
            unit_2.is_alive = False
            result = True
            break
        unit_1.health = unit_1.health - unit_2.attack
        if unit_1.health < 0:
            unit_1.is_alive = False
            result = False
            break
    return result

w = Warrior()
k = Knight()

print(fight(w,k))
