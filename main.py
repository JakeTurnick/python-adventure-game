import time
from colorama import init, Fore, Style
init(autoreset=True)
from rm1 import rm1_class
import rm2
import rm3


class Main_Game:
    # starting game

    def __init__(self, key=0):

        def green_text(message):
            for c in message:
                print(Fore.GREEN + c, end='')
                time.sleep(0.01)
        print(Style.RESET_ALL, end='')

        green_text("You slowly come too, you've been unconsious for some time. \nHow long, you're not sure.  \n")
        time.sleep(3)
        green_text("You look around. \nYou're in your car but you've wrecked. \nAll you remember is you heard a 'pop' and you lost control. \nIt seems a tree limb pierced the windshield, cracking it... \n")
        time.sleep(6)

        self.key = key


    def start_room(self):
        room_choice = input(
            "Which room would you like to enter? (rm1/rm2/rm3)")

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
