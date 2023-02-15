

class Hero:
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti


class Hero_super(Hero):
    def __init__(self, name, abyliti):
        Hero.__init__(self, name, abyliti)

    def __str__(self):
        return f'name is: {self.name}\n' \
               f'abyliti is: = {self.abyliti}'

    def prints(self):
        print(f'name is {self.name} it is super_hero')


# first = Hero_super("Супермен", "летать")
# first.prints()


