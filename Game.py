import random


class Game:
    def __init__(self):
        self.Data = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.round_count = 1

    def validation(self):
        one_player = input('Introducing you selected: ').lower()
        if one_player not in self.Data:
            print('Invalid input. Please try again.')
            return self.validation()
        return one_player

    def War(self):
        while self.round_count <= 3:
            print(f'Round {self.round_count}')
            player_choice = self.validation()
            computer_choice = random.choice(self.Data)
            if player_choice == computer_choice:
                print("Drawing")
            elif (player_choice == 'rock' and computer_choice == 'scissors') or \
                 (player_choice == 'scissors' and computer_choice == 'paper') or \
                 (player_choice == 'paper' and computer_choice == 'rock'):
                print('You win this round!')
                self.player_score += 1
            else:
                self.computer_score += 1
                print('Computer wins this round!')
            self.round_count += 1

        self.Victory()

    def Victory(self):
        if self.player_score > self.computer_score:
            print('Congratulations! You won the game!')
        else:
            print('Computer won the game!')


starting = Game()
starting.War()
