#!/usr/bin/env python3
# Write your code here
from random import choice
from os import path
from sys import stderr


class RockPaperScissors:
    options = dict()
    points = {'Draw': 50, 'Win': 100}
    current_scores = {}

    def __init__(self, name):
        self.name = name
        print(f'Hello, {self.name}')
        self.def_options = 'rock', 'paper', 'scissors'
        if self.name not in self.current_scores:
            self.current_scores[self.name] = 0

    def set_options(self):
        options = input()
        if options:
            self.def_options = tuple(options.split(','))
        self.weaker_options()
        print("Okay, let's start")

    def weaker_options(self):
        for n in range(len(self.def_options)):
            user_options = self.def_options[n + 1:] + self.def_options[:n]
            wins_over = user_options[len(user_options) // 2:]
            self.options[self.def_options[n]] = wins_over

    def load_scores(self):
        with open('rating.txt', 'r+') as rating:
            for lines in rating.readlines():
                self.current_scores[lines.split()[0]] = int(lines.split()[1])
            if not rating.read():
                print(f'{self.name} 0', file=rating, flush=True)

    def save_score(self):
        if not path.exists('rating.txt'):
            open('rating.txt', 'w').close()
        with open('rating.txt', 'w+') as score:
            for k, v in self.current_scores.items():
                print(f'{k} {v}', file=score, flush=True)

    def input_check(self, opt):
        if opt not in self.def_options:
            print('Invalid input', file=stderr)
            return False
        return True

    def who_won(self, usr_input, computer):
        if computer == usr_input:
            print(f'There is a draw ({usr_input})')
            self.current_scores[self.name] += self.points['Draw']
        elif computer in self.options[usr_input]:
            print(f'Well done. Computer chose {computer} and failed')
            self.current_scores[self.name] += self.points['Win']

        else:
            print(f'Sorry, but computer chose {computer}')

    def game(self):
        self.load_scores()
        self.set_options()
        self.save_score()
        inp = input()
        while inp != '!exit':
            if inp == '!rating':
                print(f'Your rating: {self.current_scores.get(self.name)}')
            elif self.input_check(inp):
                self.who_won(inp, choice(self.def_options))
            inp = input()
        self.save_score()
        print('Bye!')


rpc = RockPaperScissors(input('Enter your name: '))
rpc.game()
