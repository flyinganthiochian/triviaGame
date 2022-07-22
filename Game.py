from Test import *
from Player import *
class Game:
    #this is the main .py file
    def __init__(self):
        print("\n ***Welcome to the Trivia Game***") 
        self.player_list = []
        

    def play_game(self):
        self.set_number_of_players()
        self.add_players()

    

    def set_number_of_players(self):
        number_of_players_string = input("How Many Players will play the Game? : ")
        while not number_of_players_string.isnumeric():
            print("\n Opps that's not an integer! Please enter a valid Number: \n")
            number_of_players_string = input("How Many Players will play the Game? : ")
        self.number_of_players = int(number_of_players_string)
    
    
    def add_players(self):
        for player in range(self.number_of_players):
            print("\nPlayer {0} ".format(str(player+1)))
            Player.add_player_to_game(self)

        

        




