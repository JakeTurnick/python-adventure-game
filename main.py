import rm3
import rm2
from rm1 import rm1_class
import time
from colorama import init, Fore, Style
init(autoreset=True)

# LOADING = no story here yet :(


class Main_Game:
    # starting game

    def __init__(self, key=0):
        self.key = key

        COLOR = [Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

        skip = input("would you like to skip intro (for testing)? (y/n) : ")
        if skip == "y":
            room_sel = input("which room would you like to test (1, 2, 3) : ")
            if room_sel == "3":
                print("keys before rm3: ", self.key)
                rm3.Garage.play_garage(self.key)  # imported
                print("keys after rm3: ", self.key)

    # print_slow("message", COLOR['x']) slows the speed of text
    # place index value from array above inside [] to choose color

        def print_slow(message, COLOR):
            for c in message:
                print(COLOR + c, end='')
    # change speed of text below -> set to 0.1 for live review
                time.sleep(0.01)
        print(Style.RESET_ALL, end='')

    # intro text
        print_slow(
            ("You slowly come too, you've been unconsious for some time. \nHow long, you're not sure...  \n"), COLOR[0])
        time.sleep(3)

        print_slow(
            ("You look around. \nYou're in your car but you've wrecked. \nAll you remember is you heard a 'pop' and you lost control. \nIt seems a tree limb pierced the windshield, cracking it... \n"), COLOR[0])
        time.sleep(3)

        #list of starting choices:
        car_or_myself = []
        #run loop while len (length of list) < 2
        while len(car_or_myself) < 2:
            choose_start = input("Would you like to inspect yourself or the car? (Type: MYSELF or CAR) \n").upper()
            if choose_start in ["MYSELF", "CAR"]:
                if choose_start in car_or_myself:
                    self.print_slow(("You have already selected " + choose_start + ".\n"), self.COLOR[0])
                    time.sleep(3)
                else:
                    car_or_myself.append(choose_start)
                    if choose_start == "MYSELF":
                        self.print_slow(("Your head hurts, you believe you have a concusion. \nYour thoughts are foggy and it's difficult to complete a coherent thought. \nYou have a small gash on your forehead. The bleeding has almost stopped. \nYou should find a gauze to wrap around the wound...\n"), self.COLOR[0])
                        time.sleep(3)
                    elif choose_start == "CAR":
                        self.print_slow(("You chose car...LOADING \n"), self.COLOR[0])
                        time.sleep(3)
            else:
                self.print_slow(("Please type 'MYSELF' or 'CAR' to continue... \n"), self.COLOR[0])
                time.sleep(3)

        #call for help:
        call_for_help = []
        while len(call_for_help) < 2:
            choose_call_for_help = input(f"You find your phone in the car. \nWho do you call? (Options: 911 or LINDA, your wife...\n").upper()
            if choose_call_for_help in ["LINDA", "911"]:   
                if choose_call_for_help in call_for_help:
                    self.print_slow(("You have already selected " + choose_call_for_help + ".\n"), self.COLOR[0])
                    time.sleep(3)
                else:
                    call_for_help.append(choose_call_for_help)
                    if choose_call_for_help == "LINDA":
                        print("LOADING...Linda...no response \n")
                    elif choose_call_for_help == "911":
                        print("LOADING...911...no response \n")
            else:
                self.print_slow(("Please type '911' or 'Linda' to continue... \n"), self.COLOR[0])
                time.sleep(3)

        self.print_slow(("No one answers the phone... \nYou notice the sun is setting, it's starting to get foggy... \n You also notice a small town in the distance... \n "), self.COLOR[0])

        choose_wait_or_walk = ["WALK", "WAIT"]
        wait_or_walk = input(f"Do you want to WALK to town or WAIT for help?\n").upper()
        if wait_or_walk in choose_wait_or_walk:
            if wait_or_walk == "WALK":      
                self.print_slow(("You decide to walk to town...\n"), self.COLOR[0])
                time.sleep(3)
            if wait_or_walk == "WAIT":
#IMPORTANT !! ADD OPTION TO END GAME HERE AFTER COMPLETE        
                self.print_slow(("You decide to wait for help\nwaiting...\nwaiting...\nwaiting...\n...oh no...\na grizzly bear finds you and eats you! \nGAME OVER\n"), self.COLOR[0])
                return
        else:
            self.print_slow(("Please choose 'WALK' or 'WAIT' to continue... \n"), self.COLOR[0])
            time.sleep(3)

    def start_room(self):
        room_choice = input(
            "Which room would you like to enter? (rm1/rm2/rm3)\n")

        if room_choice == "rm1":
            rm1_class(self.key).play_room_one()  # imported
            # instanciate rm1 with key from Main_Game & call play room
        elif room_choice == "rm2":
            rm2.rm2.play_room_two()  # imported
        else:
            print("keys before rm3: ", self.key)
            rm3.Garage.play_garage(self.key)  # imported
            print("keys after rm3: ", self.key)

    # while keys < 3:
        # prompt choice

    # def end:
        # putting car pieces in and leaving

    def end_room():
        pass

    # if keys > 3:
        # end function


new_game = Main_Game()
new_game.print_intro()
new_game.start_room()
