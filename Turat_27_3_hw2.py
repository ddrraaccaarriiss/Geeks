import math
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return print(f'name is: {self.name}')

    def change_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f'nickname is {self.nickname}\n' \
               f'superpower is {self.superpower}\n' \
               f'health points = {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)




super_hero = SuperHero('Кларк', 'Супермен', 'лазер', 100, 'Против зла!')
super_hero.get_name()
super_hero.change_health_points()
print(f'length of the catchphrase is {super_hero.__len__()}')
print(super_hero)


class Sky(SuperHero):
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        # super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def change_health_points(self):
        self.health_points *= self.health_points
        self.fly = True
    def printfly(self):
        print(f'{self.fly} fly in the True_phrase ')
    # def crit(self):
    #     print(f"exponentiated damage: {math.pow(self.damage, self.damage)}")
    #
    #

sky_hero = Sky('Bruce Wayne', 'Batman', 'Money', 100, 'I am Batman!',3)
sky_hero.change_health_points()
sky_hero.printfly()
## sky_hero.crit()
print(sky_hero)

class Space(SuperHero):
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly =False ):
        # super().__init__(name,nickname, superpower, health_points, catchphrase)
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def change_health_points(self):
        self.health_points *= self.health_points
        self.fly = True

    def printfly(self):
        print(f'{self.fly} fly in the True_phrase ')

    # def crit(self):
    #     print(f"exponentiated damage: {math.pow(self.damage, self.damage)}")
    #

space_hero = Space('Дейдара', 'Аниме персонаж', 'взрыв', 100, 'Искуство это взрыв!',4)
space_hero.change_health_points()
space_hero.printfly()
# space_hero.crit()
print(space_hero)


class Villain(Space):
    people = "monster"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        Space.__init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly)


    def gen_x(self):...
    def crit(self):
        print(f" {self.name } exponentiated damage: {math.pow(self.damage, self.damage)}")
        # print(pow(self.damage , self.damage ))
        # self.damage = self.damage ** 5


villain_hero = Villain("Виллиан", "Выдуманный герой", "Уроган",100,"Делай добро",3)
print(villain_hero)
villain_hero.crit()
Villain.crit(space_hero)
Villain.crit(sky_hero)




