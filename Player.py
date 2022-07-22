from Game import *
class Player:
    id=0
    

    def __init__(self, name): 
        self.name=name
        self.score=0
        Player.id +=1
        self.id=Player.id
        
    
    def get_player_name():
        return input("Please enter your name: ")
    
    def add_player_to_game(game):
        player_to_add= Player(Player.get_player_name())
        game.player_list.append(player_to_add)


    