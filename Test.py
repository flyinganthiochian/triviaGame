from Game import *
from Player import *
class Test:
    #all the test related methods are defined under Test class
    pass

    def test_print_players(self,game):
        print("Name of the Players Are: ")
        for player in game.player_list:
            print("name: {0} id: {1}".format(player.name,str(player.id)))
           


