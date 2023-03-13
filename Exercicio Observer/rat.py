from game import Game


class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.attack: int = 1

        self.game.rat_enters.append(self.rat_enters)
        self.game.notify_rat.append(self.notify_rat)

        self.game.rat_enters(self)


    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(self)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1