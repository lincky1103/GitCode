from sys import exit
from random import randint

class Game(object):
    def __init__(self, start):
        self.quips = [
            'You Die!',
            'Loser!',
            'Good luck next time!'
        ]

        self.start = start
    
    def play(self):
        next = self.start

        while True:
            print('\n---------')
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0,len(self.quips)-1)])
        exit(1)

    def princess_room(self):
        print('Princess gives you a cake, eat it or not?')

        eat_it = input('> ')

        if eat_it == 'eat it':
            print('You explode like a frog!')
            
            return('death')
    
        elif eat_it == 'do not eat it':
            print('Bad manner!')

            return('death')

        elif eat_it == 'make her eat it':
            print('Princess smiles and shows you a door, open it.')

            return('gold_pool')

        else:
            print('Don\'t make princess wait.')

            return('princess_room')

    def gold_pool(self):
        print('You win!')

a_game = Game('princess_room')
a_game.play()   
