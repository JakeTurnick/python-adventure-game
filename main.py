import time
from colorama import init, Fore, Style
init(autoreset=True)
from rm1 import rm1_class
import rm2
import rm3

#LOADING = no story here yet :(

class Main_Game:
    # starting game


    def __init__(self, key=0):
        self.key = key
        
        COLOR = [Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        
    #print_slow("message", COLOR['x']) slows the speed of text
    #place index value from array above inside [] to choose color
        def print_slow(message, COLOR):
            for c in message:
                print(COLOR + c, end='')
    #change speed of text below -> set to 0.1 for live review
                time.sleep(0.01)
        print(Style.RESET_ALL, end='')

    #intro text
        print_slow(("You slowly come too, you've been unconsious for some time. \nHow long, you're not sure...  \n"), COLOR[0])
        time.sleep(3)
        
        print_slow(("You look around. \nYou're in your car but you've wrecked. \nAll you remember is you heard a 'pop' and you lost control. \nIt seems a tree limb pierced the windshield, cracking it... \n"), COLOR[0])
        time.sleep(3)

    #starting choices:
        choose_start = input("Would you like to inpsect yourself or the car first? (Type: MYSELF or CAR) \n")
        if choose_start.upper() == "MYSELF":
            print_slow(("Your head hurts, you believe you have a concusion. \nYour thoughts are foggy and it's difficult to complete a coherent thought. \nYou have a small gash on your forehead. The bleeding has almost stopped. \nYou should find a gauze to wrap around the wound...\n"), COLOR[0])
            time.sleep(3)
    #name 'str' for other option (see 'choose_start_alt') w/ 'start_other'
            start_other = "CAR"
        elif choose_start.upper() == "CAR":
    #left 'LOADING' to fill in later 
            print_slow(("You chose car...LOADING \n"), COLOR[0])
            time.sleep(3)
            start_other = "MYSELF"
    #trying to figure out how we can loop this back to the start if player does not make a choice?
        elif choose_start_alt != "MYSELF" or "CAR":
            print_slow(("Please type MYSELF or CAR to continue... \n"), COLOR[0])
            time.sleep(3)
    #option to pick alternative option...
        choose_start_alt = input(f"Would I like to inpsect {start_other}? (Type: {start_other}) \n")
        if choose_start_alt == "MYSELF":
            print_slow(("Your head hurts, you believe you have a concusion. \nYour thoughts are foggy and it's difficult to complete a coherent thought. \nYou have a small gash on your forehead. The bleeding has almost stopped. \nYou should find a gauze to wrap around the wound\n"), COLOR[0])
            time.sleep(3)
        elif choose_start_alt == "CAR":
            print_slow(("You chose car...LOADING \n"), COLOR[0])
            time.sleep(3)
        elif choose_start_alt != "MYSELF" or "CAR":
            print_slow(("...LOADING \n"), COLOR[0])
            time.sleep(3)

        choose_call_for_help = input(f"You find your phone in the car. \nWho do you call first? (Options: 911 or LINDA, your wife...\n")
        if choose_call_for_help == "911":    
            print("LOADING... \n")
        elif choose_call_for_help == "LINDA":
            print("LOADING... \n")

    def start_room(self):
        room_choice = input(
            "Which room would you like to enter? (rm1/rm2/rm3)\n")

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
