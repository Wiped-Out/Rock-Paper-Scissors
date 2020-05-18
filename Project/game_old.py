#!/usr/bin/env python3
# # Write your code here
from random import choice
from os import path


class RockPaperScissors:
    options = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors', '!rating': '!rating', '!exit': 'Bye!'}
    points = {'Draw': 50, 'Win': 100}
    current_scores = {}

    def __init__(self, name):
        self.computer = choice(('rock', 'paper', 'scissors'))
        self.name = name
        print(f'Hello, {self.name}')
        if not path.exists('rating.txt'):
            open('rating.txt', 'w').close()
        if self.name not in self.current_scores:
            self.current_scores[self.name] = 0
        self.checker()

    def checker(self):
        with open('rating.txt') as rating:
            for lines in rating.readlines():
                self.current_scores[lines.split()[0]] = lines.split()[1]

    def game(self, inp):
        if inp not in self.options:
            print('Invalid input')
        elif inp == '!rating':
            print(f'Your rating: {self.current_scores.get(self.name)}')
        elif inp == '!exit':
            print('Bye!')
            exit()
        elif self.computer == inp:
            print(f'There is a draw ({inp})')
            self.current_scores[self.name] += self.points['Draw']
        elif self.options.get(self.computer) != inp:
            print(f'Sorry, but computer chose {self.computer}')
        else:
            print(f'Well done. Computer chose {self.computer} and failed')
            self.current_scores[self.name] += self.points['Win']


rpc = RockPaperScissors(input('Enter your name: '))
while True:
    rpc.game(input())

