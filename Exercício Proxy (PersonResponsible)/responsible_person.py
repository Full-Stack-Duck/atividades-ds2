from person import Person

class PersonProxy:
    def __init__(self, age: int):
        self.person = Person(age)

    def drink(self):
        if self.person.age >= 18:
            return self.person.drink()
        else:
            return 'Desculpe, você não tem idade suficiente para beber'

    def drive(self):
        if self.person.age >= 16:
            return self.person.drive()
        else:
            return 'Foi mal, você não tem idade para dirigir'

    def drink_and_drive(self):
        return 'Sinto muito, você dirigiu bêbado e acabou morrendo'