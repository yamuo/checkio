import copy

class Warrior:
    health = 50
    attack = 5
    is_alive = True
    
class Knight(Warrior):
    attack = 7

class Army:
    def __init__(self):
        self.units = []
        
    def add_units(self,unit,count):
        if unit == Warrior:
            for i in range(count):
                u = Warrior()
                self.units.append(copy.deepcopy(u))
        if unit == Knight:
            for i in range(count):
                u = Knight()
                self.units.append(copy.deepcopy(u))

    
def fight(unit_1, unit_2):
    result = True
    
    while unit_1.is_alive and unit_2.is_alive:
        
        unit_2.health = unit_2.health - unit_1.attack
        if unit_2.health <= 0:
            unit_2.is_alive = False
            result = True
            break
        
        unit_1.health = unit_1.health - unit_2.attack
        if unit_1.health <= 0:
            unit_1.is_alive = False
            result = False
            break
        
    return result

class Battle:
    def fight(self,army_1,army_2):
        result = False
        for i in army_1.units:
            for j in army_2.units:
                if i.is_alive and j.is_alive:
                    result = fight(i,j)

        return result
    

if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)
    battle = Battle()
    print(battle.fight(army_1, army_2))