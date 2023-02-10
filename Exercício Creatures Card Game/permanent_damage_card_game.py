from card_game import CardGame
from creature import Creature


class PermanentDamageCardGame(CardGame):

    def hit(self, attacker: Creature, defender: Creature):
        defender.health -= attacker.attack
        
        print('=' * 15, 'PERMANENT DAMAGE HIT', '='*15)
        print(f'{attacker.name} causou {attacker.attack} de dano em {defender.name}')
        print(f'HP atual do {defender.name}: {defender.health}')