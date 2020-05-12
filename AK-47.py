
class Soldier:
    def __init__(self, name):
        self.name = name 
    
class Guns:
    def __init__(self):
        self.bullets = 30
    
    def AK47(self):
        print(f'Soldier {self.name.title()} is ready to shoot')
        print(f'{self.name.title()} is ordered to shoot:')
        print('AK47 Makes a sound:')
        if self.bullets:
            shooting_num = 0
            for i in range(self.bullets):
                shooting_num += 1
                self.bullets -= 1
                print("tigi-tigitishh ", shooting_num, ' times')
        else:
            print('No bullets in the amo')

    def bullets_num(self):
        print(f'{self.bullets} are left in the amo')

    def reload(self):
        if self.bullets == 0:
            self.bullets = 30
            print(f"{self.name.title()} shouts 'REALOAD!'")
            print(f'The number of bullets in the amo is {self.bullets}')

class Act_of_Shooting(Guns, Soldier):
    def __init__(self,name):
        Soldier.__init__(self,name)
        Guns.__init__(self)
        # print(f"\t\t\tBullets: {self.bullets} pieces")

Soldier = Act_of_Shooting("John")
Soldier.AK47()
Soldier.reload()
