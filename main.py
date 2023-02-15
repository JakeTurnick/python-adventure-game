import rm3
import rm2
import rm1
from rm1 import rm1_class
import time
from colorama import init, Fore, Style
init(autoreset=True)

# LOADING = no story here yet :(


class Main_Game:
    # defining our keys to victory
    def __init__(self, key=1):
        self.key = key
        self.life = True

    COLOR = [Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    # print_slow("message", COLOR['x']) slows the speed of text
    # place index value from list above inside [] to choose color

    def print_slow(self, message, COLOR):
        for c in message:

            print(COLOR + c, end='', flush=True)
    # change speed of text below -> set to 0.1 for live review
            time.sleep(0.01)
            print(Style.RESET_ALL, end='', flush=True)

    def test(self):
        while self.life == True:
            rm_choice = input("select a room (1/2/3/test)\n")
            while rm_choice != "1" and rm_choice != "2" and rm_choice != "3" and rm_choice != "test":
                # only if it's a choice we want
                rm_choice = input("select a room (1/2/3)\n")

            if rm_choice == "1":
                print(f"You had {self.key} keys")
                var = rm1.rm1_class(self).play_room_one()
                # rm1_class(self).play_room_one()
                self.key = var["key"]
                self.life = var["life"]
                print(
                    f"You now have {self.key} keys and life: {self.life}")
                if self.life == False:
                    print("You died")
                # while rm1.rm1_class(self).complete() == True:
                #     self.test()
                # rm 1

            elif rm_choice == "2":

                print(f"You had {self.key} keys")
                var = rm2.rm2(self).play_market()
                self.key = var["key"]
                self.life = var["life"]
                print(f"You now have {self.key} keys and are {self.life}")
                if self.life == False:
                    print("You died")
        elif rm_choice == "3":
            var = rm3.Garage_class(self).play()
            self.key = var["key"]
            self.life = var["life"]
            print(f"You now have {self.key} keys")
            if self.life == False:
                print("You died")
        elif rm_choice == "test":
            # THIS WORKS! Make sure your room does 2 things if you win:
            # self.key += 1 // return self.key
            while self.life == True:
                print(f"You had {self.key} keys")
                # <-- check this function to better understand
                var = rm3.Garage(self).play_room_three()
                # Var is a dictionary with 2 keys(key & life) which are the values -
                # returned from the play function (self.key, self.life)
                self.key = var["key"]
                self.life = var["life"]
                print(f"You now have {self.key} keys")
            if self.life == False:
                print("You died")

    def play_main(self):
        self.print_intro()
        while self.life == True:
            room_choice = input(
                "Which room would you like to enter? (rm1/rm2/rm3)\n")

            while room_choice != "rm1" and room_choice != "rm2" and room_choice != "rm3":
                room_choice = input(
                    "Which room would you like to enter? (rm1/rm2/rm3)\n")

            if room_choice == "rm1":
                print(f"You now have {self.key} keys")
                rm1_class(self.key).play_room_one()  # imported
                # instanciate rm1 with key from Main_Game & call play room
                print(f"You now have {self.key} keys")
            elif room_choice == "rm2":
                rm2.rm2(self.key).play_market()  # imported
            else:  # room_choice == "rm3"
                var = rm3.Garage(self).play()
                # Var is a dictionary with 2 keys(key & life) which are the values -
                # returned from the play function (self.key, self.life)
                self.key = var["key"]
                self.life = var["life"]

            # after each room - if statement to check if life == False & break
            # rm3(self).play
        if self.keys > 3:
            self.end_room()

# intro text
    def print_intro(self):
        self.print_slow(
            ("You slowly come too... \nyou've been unconsious for some time... \nHow long, you're not sure...  \n"), self.COLOR[0])
        time.sleep(3)
        self.print_slow(
            ("You look around... \nYou're in your car but you've wrecked. \nAll you remember is you heard a 'pop' and you lost control... \nIt seems a tree limb pierced the windshield, cracking it... \n"), self.COLOR[0])
        time.sleep(3)

# intro/choose between inspecting yourself and the car:
        car_or_myself = []
        # run loop while len (length of list) < 2
        while len(car_or_myself) < 2:
            choose_start = input(
                "Would you like to inspect yourself or the car? (Type: MYSELF or CAR) \n").upper()
            if choose_start in ["MYSELF", "CAR"]:
                if choose_start in car_or_myself:
                    self.print_slow(
                        ("You have already selected " + choose_start + ".\n"), self.COLOR[0])
                    time.sleep(3)
                else:
                    car_or_myself.append(choose_start)
                    if choose_start == "MYSELF":
                        self.print_slow(
                            ("Your head hurts, you believe you have a concusion. \nYour thoughts are foggy and it's difficult to complete a coherent thought. \nYou have a small gash on your forehead. The bleeding has almost stopped. \nYou should find a gauze to wrap around the wound...\n"), self.COLOR[0])
                        time.sleep(3)
                    elif choose_start == "CAR":
                        self.print_slow(
                            ("You chose car...LOADING \n"), self.COLOR[0])
                        time.sleep(3)
            else:
                self.print_slow(
                    ("Please type 'MYSELF' or 'CAR' to continue... \n"), self.COLOR[0])
                time.sleep(3)

# player tries to call for help, unable to:
    # def start_choice(self):
        call_for_help = []
        while len(call_for_help) < 2:
            choose_call_for_help = input(
                f"You find your phone in the car. \nWho do you call? (Options: 911 or LINDA, your wife...\n").upper()
            if choose_call_for_help in ["LINDA", "911"]:
                if choose_call_for_help in call_for_help:
                    self.print_slow(
                        ("You have already selected " + choose_call_for_help + ".\n"), self.COLOR[0])
                    time.sleep(3)
                else:
                    call_for_help.append(choose_call_for_help)
                    if choose_call_for_help == "LINDA":
                        print("LOADING...Linda...no response \n")
                    elif choose_call_for_help == "911":
                        print("LOADING...911...no response \n")
            else:
                self.print_slow(
                    ("Please type '911' or 'Linda' to continue... \n"), self.COLOR[0])
                time.sleep(3)

        self.print_slow(
            ("No one answers the phone... \nYou notice the sun is setting, it's starting to get foggy... \n You also notice a small town in the distance... \n "), self.COLOR[0])

# Player chooses to WALK to town or WAIT for help and die
        choose_wait_or_walk = ["WALK", "WAIT"]
        wait_or_walk = input(
            f"Do you want to WALK to town or WAIT for help?\n").upper()
        if wait_or_walk in choose_wait_or_walk:
            if wait_or_walk == "WALK":
                self.print_slow(
                    ("You decide to walk to town...\nYou see three buildings in front of you... \na clinic, a market, and a garage...\n no one in sight...\n"), self.COLOR[0])
                time.sleep(3)
            if wait_or_walk == "WAIT":
                # IMPORTANT !! ADD OPTION TO END GAME HERE AFTER COMPLETE
                self.print_slow(
                    ("You decide to wait for help\nwaiting...\nwaiting...\nwaiting...\n...oh no...\na grizzly bear finds you and eats you! \nGAME OVER\n"), self.COLOR[0])
                print("GAME OVER")
                self.life = False
                return {"key": self.key, "life": self.life}
        else:
            self.print_slow(
                ("Please choose 'WALK' or 'WAIT' to continue... \n"), self.COLOR[0])
            time.sleep(3)

# Player chooses between 3rms or BUILDINGS

    # ...

# Player obtains keys from all 3rms
# Game ends here
    def end_room(self):
        pass

        if self.keys > 3:
            print("You've collected all the parts needed to fix your car")
            print("After your trials through the clinic, market, and garage, you're finally able to fix your car and get out of here.")
            print("This towns gone crazy, and it's far too much. You're just one person, you make your way back to the your vehicle.")
            print("By the time the radiator and your tire is fixed, the sun is beginning to set. You turn your car around and leave")
            print(
                "May God have mercy on your soul and everyones soul who was in that town...")
        # end function


new_game = Main_Game()
new_game.test()
# new_game.play_main()
