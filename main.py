from rm1 import rm1_class
import rm2
import rm3


class Main_Game:
    # starting game
    def __init__(self, key=0):
        self.key = key

    def start_room(self):
        room_choice = input(
            "which room would you like to enter? (rm1/rm2/rm3)")

        if room_choice == "rm1":
            rm1_class(self.key).play_room_one()  # imported
            # instanciate rm1 with key from Main_Game & call play room
        elif room_choice == "rm2":
            rm2.rm2.play_room_two()  # imported
        else:
            rm3.rm3.play_room_three()  # imported

    # while keys < 3:
        # prompt choice

    # def end:
        # putting car pieces in and leaving

    def end_room():
        pass

    # if keys > 3:
        # end function


new_game = Main_Game()
new_game.start_room()
