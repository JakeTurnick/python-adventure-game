# Jake's room - Mechanics garage
# Goal: Obtain fresh Tire
# - Tire: Obtain Socket Wrench
# -- Socket wrench: Locked inside car with zombie
# --- Car key: Riddle from accounting
# --- Crowbar: Found in storage
# -- No crowbar? 50% chance of death
# -- Crowbar? Hold zombie back and grab socket wrench

from time import sleep
from colorama import init, Fore, Style


class Garage_class:
    # key, life
    def __init__(self, main):
        # main variables
        self.key = main.key
        self.life = main.life
        self.win = False
        # garage key items
        self.flash_light = False
        self.car_key = False
        self.crowbar = False
        self.socket_wrench = False
        self.tire = False
        # keeping track of encounters
        self.car_encounter = False
        self.tire_encounter = False

    COLOR = [Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    def print_slow(self, COLOR, speed, message):
        for c in message:

            print(COLOR + c, end='', flush=True)
    # change speed of text below -> set to 0.1 for live review
            sleep(speed)
            print(Style.RESET_ALL, end='', flush=True)

    def test_garage(self):
        self.print_slow(self.COLOR[3], .01, "you enter the garage \n")
        self.print_slow(
            self.COLOR[3], .01, "as if the scenery is enough, the smell of blood lingers in the air \n")
        print("you spot a key with a note propped up near it on a counter \n")
        test_input = input("Would you you like a key? (y/n)\n ")

        if test_input.lower() == "y":
            print(
                "you graciously accept the key, thankful for the hardwork and blood shed to get it here \n")
            self.key += 1
            return {"key": self.key, "life": self.life}

        else:
            print("begrudgingly you take the key")
            self.key += 1
            return {"key": self.key, "life": self.life}

    def ded(self):
        self.life = False

    def play(self):
        self.entrance()
        if self.win == True:
            return {"key": self.key, "life": self.life}

    def entrance(self):
        self.print_slow(
            self.COLOR[3], .05, "You enter the garage, the lights appear to be out but the store front windows allow you to see\n")
        sleep(.5)
        self.print_slow(
            self.COLOR[3], .05,  "You walk up to the counter and peak around . . . No one seems to be aronud\n")
        sleep(.5)
        self.print_slow(
            self.COLOR[4], .05, "As you scan the room you spot a door labeled \"Garage\" and what could be supplies littered behind the counter\n")
        scan_entrance = input(
            "What do you check? (\"counter\" or \"garage\") \n")
        while scan_entrance.lower() != "counter" and scan_entrance.lower() != "garage" and scan_entrance.lower() != "t":
            scan_entrance = input(
                "Invalid input - What do you check? (\"counter\" or \"garage\") \n")
        if scan_entrance.lower() == "t":
            self.check_car()
        elif scan_entrance.lower() == "counter":
            self.print_slow(
                self.COLOR[4], .05, "You see a flashlight and batteries behind the counter... almost like someone dropped them\n")
            sleep(.5)
            take_light = input("Take the flashlight? (y/n) : \n")

            while take_light.lower() != "y" and take_light.lower() != "n":
                take_light = input(
                    "Invalid input - Take the flashlight? (y/n) : \n")

            if take_light.lower() == "y":
                self.print_slow(
                    self.COLOR[3], .05, "You step behind the counter and pick up the flashlight\n")
                sleep(.5)
                self.flash_light = True
                self.print_slow(
                    self.COLOR[0], .05, "You turn the light on to verify that it works . . . it does!\n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[1], .08, "But you spot the flash lights reflection on a pool of some viscous liquid\n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[1], .08, "... it's probablt oil . . . hopefully\n")
                sleep(.8)
                self.print_slow(
                    self.COLOR[3], .05, "With a flashlight equipped you feel ready to enter the garage\n")
                sleep(1)

            else:  # take_light == n
                self.print_slow(
                    self.COLOR[0], .05, "A bold and brash adventurer like you don't need no damn lights\n")
                sleep(.5)
        elif scan_entrance.lower() == "garage":  # scan_entrance == garage
            self.print_slow(
                self.COLOR[3], .05, "With no fear, you plunge yourself into the dark garage \n")
            sleep(.5)
            self.garage_intro()

        # after counter
        if self.flash_light == True:
            self.print_slow(
                self.COLOR[3], .05, "You use flashlight to help you see in the large garage \n")
            sleep(.5)
            self.garage_intro()

        else:  # scan_entrance == garage
            self.print_slow(
                self.COLOR[3], .05, "With no fear, you plunge yourself into the dark garage \n")
            sleep(.5)
            self.garage_intro()

    def garage_intro(self):
        if self.flash_light == True:
            self.print_slow(self.COLOR[3], .05,
                            "You open the door to the garage \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[1], .05, "As you scan the room with light you think you hear the sound of shuffling... but it quickly dies down... \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[3], .05, "The garage seems to be a large working area for mechanics with doors to various rooms \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[4], .05, "Using your flaslight you find the doors are clearly labeled \n\"Entrance\" \"Office\" \"Storage\"  \n")
        else:
            self.print_slow(
                self.COLOR[3], .05, "The garage is dark without a flashlight \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[3], .05, "You grope around the walls hoping to find a door... \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[3], .02, ". . . you hear a small crash as something dropped in the garage \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[3], .02, "...the sounds of someone struggling can be heard... \n")
            sleep(.5)
            self.print_slow(
                self.COLOR[4], .05, "you come to a junction of doors... in the limited visibility you make out the words \n")
            sleep(.5)
            self.print_slow(self.COLOR[4], .05,
                            "\n\"Entrance\" \"Office\" \"Storage\"\n")
            sleep(.5)
        self.garage()

    def garage(self):
        room_choice = input(
            "What do you explore? (\"garage\" \"office\" \"storage\") \n")
        while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
            room_choice = input(
                "What do you explore? (\"garage\" \"office\" \"storage\") \n")
        if room_choice.lower() == "garage":
            if self.car_encounter == False:
                if self.flash_light == True:
                    self.print_slow(
                        self.COLOR[3], .05, "You walk around the garage, it feels as if life suddenly stopped... \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, "Cars are still lifted to be worked on, the occasional oil puddle is present... but nothing looks put away... \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[0], .05, "A tire pile! You approach hoping to find a replacement for your car \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, ". . . tires... but no wrench to install them... better keep looking \n")
                    sleep(.5)
                    self.check_car()
                    return

                else:  # flash_light == False
                    self.print_slow(
                        self.COLOR[3], .05, "You hug the outside wall of the garage... You hear strange sounds coming from it's large rolling doors \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, "The sound of a struggle is growing louder as you creep to the back of the garage \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[1], .005, """
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    !! You tumble over something !!
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                     \n""")
                    sleep(.5)
                    self.print_slow(self.COLOR[1], .05, ". . . Tires!?")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[0], .05, "You feel a large pile of tires in front of you! The bolts are locked in \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[4], .05, "I should find some kind of wrench \n")
                    sleep(.5)
                    self.check_car()
                    return
            elif self.car_encounter == True:
                self.check_car()

        elif room_choice.lower() == "office":
            self.office()
            return
        elif room_choice.lower() == "storage":
            self.storage()
            return
        elif room_choice.lower() == "hey":
            self.print_slow(self.COLOR[3], .05,
                            "You utter a greeting to the void \n")
            self.print_slow(self.COLOR[3], .25, ". . . h . e . l . l . o . .")
            return

    def check_car(self):
        if self.car_encounter == False:
            if self.flash_light == True:
                if self.car_key == False:
                    self.print_slow(
                        self.COLOR[3], .05, "you spot a lowered car with tools scattered around it, maybe I'll find a wrench there \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, "nothing of use appears to be on the ground, you try to open the car but it's locked \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, "peering in with eyes cupped to the window & flashing held up you look inside \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[0], .02, "A socket wrench on the seat! The door is locked, I should find a key- \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[1], .005, """
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                     \n""")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[1], .01, "SOMETHING LEAPS AT YOU FROM INSIDE THE CAR \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[3], .05, "... it's blocked by the window but continues to struggle \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[1], .05, "a strange fluid coats the inside of the window \n")
                    sleep(.5)
                    room_choice = input(
                        "What do you explore? (\"office\" \"storage\") \n")
                    while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                        room_choice = input(
                            "What do you explore? (\"office\" \"storage\") \n")
                    if room_choice.lower() == "office":
                        self.office()
                        return
                    elif room_choice.lower() == "storage":
                        self.storage()
                        return
                elif self.car_key == True:
                    if self.crowbar == False:
                        self.print_slow(
                            self.COLOR[3], .05, "Without a weapon you tap the glass on the opposite side to get the creatures attention \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[3], .05, "running to the other side you rush to unlock the door and get the wrench \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.print_slow(
                            self.COLOR[1], .05, "You get the wrench, but not unscathed \n")
                        sleep(.5)
                        self.end()
                    elif self.crowbar == True:
                        self.print_slow(
                            self.COLOR[3], .05, "You unlock the door... crowbar in hand ready for whatever comes at you \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[1], .05, "... it's ... smiling at you? \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[1], .05, "The creature leaps at you! \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[0], .05, "but the crowbar prevents it from reaching you or blocking your path to the socket wrench \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[3], .05,
                                        "You take the wrench, slam the door and bolt away from the car \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.end()
            elif self.flash_light == False:
                if self.car_key == False:
                    self.print_slow(self.COLOR[3], .05,
                                    "you bump into a lowered car with tools scattered around it, maybe I'll find a wrench around you \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[3], .05,
                                    "nothing of use appears to be on the ground, you try to open the car but it's locked \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[3], .05,
                                    "peering in with eyes cupped to the window \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[3], .05,
                                    "your eyes adjust you see a socket wrench on the seat! I should find a key- \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[1], .005, """
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                     \n""")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[1], .01, "SOMETHING LEAPS AT YOU FROM INSIDE THE CAR \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[3], .05,
                                    "... it's blocked by the window but continues to struggle \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[1], .05, "a strange fluid coats the inside of the window \n")
                    sleep(.5)
                    room_choice = input(
                        "What do you explore? (\"office\" \"storage\") \n")
                    while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                        room_choice = input(
                            "What do you explore? (\"office\" \"storage\") \n")
                    if room_choice.lower() == "office":
                        self.office()
                        return
                    elif room_choice.lower() == "storage":
                        self.storage()
                        return
                elif self.car_key == True:
                    if self.crowbar == False:
                        self.print_slow(self.COLOR[3], .05,
                                        "Without a weapon you tap the glass on the opposite side to get the creatures attention \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[3], .05,
                                        "running to the other side you rush to unlock the door and get the wrench \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.print_slow(
                            self.COLOR[3], .05, "You get the wrench, but not unscathed \n")
                        sleep(.5)
                        self.end()
                    elif self.crowbar == True:
                        self.print_slow(self.COLOR[3], .05,
                                        "You unlock the door... crowbar in hand ready for whatever comes at you \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[1], .05, "... it's ... smiling at you? \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[1], .05, "The creature leaps at you as you open the door! \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[0], .05,
                                        "but the crowbar prevents it from reaching you or blocking your path the the socket wrench \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[3], .05,
                                        "You take the wrench, slam the door and bolt away \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.end()
        elif self.car_encounter == True:
            if self.flash_light == True:
                if self.car_key == True:
                    if self.crowbar == True:
                        self.print_slow(self.COLOR[1], .05,
                                        "You approach the sounds of struggle, muffled behind car windows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "you insert the car key into the door... The beast makes a noise as if it knowns \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "You rip the door open, shove the crowbar in, feeling the weight of the beast trying to jump at you \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "With the beast held back you grab the socket wrench, slam the door closed, and hope to never experience that again \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.end()
                    elif self.crowbar == False:
                        self.print_slow(self.COLOR[1], .05,
                                        "You approach the sounds of struggle, muffled behind car windows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "you insert the car key into the door... The beast makes a noise as if it knows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "You rip the door open, and leap for the wrench before the beast can get to you \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.print_slow(
                            self.COLOR[1], .05, "You get the wrench, but not unscathed \n")
                        sleep(.5)
                        self.end()
                elif self.car_key == False:
                    self.print_slow(
                        self.COLOR[4], .05, "I don't have the key to unlock the car \n")
                    sleep(.5)
                    room_choice = input(
                        "What do you explore? (\"office\" \"storage\") \n")
                    while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                        room_choice = input(
                            "What do you explore? (\"office\" \"storage\") \n")
                    if room_choice.lower() == "office":
                        self.office()
                        return
                    elif room_choice.lower() == "storage":
                        self.storage()
                        return
            elif self.flash_light == False:
                if self.car_key == True:
                    if self.crowbar == True:
                        self.print_slow(self.COLOR[1], .05,
                                        "You approach the sounds of struggle, muffled behind car windows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "you insert the car key into the door... The beast makes a noise as if it knowns \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "You rip the door open, shove the crowbar in, feeling the weight of the beast trying to jump at you \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "With the beast held back you grab the socket wrench, slam the door closed and hope to never experience that again \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.end()
                    elif self.crowbar == False:
                        self.print_slow(self.COLOR[1], .05,
                                        "You approach the sounds of struggle, muffled behind car windows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "you insert the car key into the door... The beast makes a noise as if it knows \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "You rip the door open, and leap for the wrench before the beast can get to you \n")
                        sleep(.5)
                        self.socket_wrench = True
                        self.print_slow(
                            self.COLOR[1], .05, "You get the wrench, but not unscathed \n")
                        sleep(.5)
                        self.end()
                elif self.car_key == False:
                    self.print_slow(
                        self.COLOR[1], .05, "I don't have the key to unlock the car \n")
                    sleep(.5)
                    room_choice = input(
                        "What do you explore? (\"office\" \"storage\") \n")
                    while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                        room_choice = input(
                            "What do you explore? (\"office\" \"storage\") \n")
                    if room_choice.lower() == "office":
                        self.office()
                        return
                    elif room_choice.lower() == "storage":
                        self.storage()
                        return

              # if self.car_encounter == True:
        # if self.car_encounter == True: skip to getting wrench

    def office(self):
        stay = True
        while stay == True:
            if self.flash_light == True:
                self.print_slow(
                    self.COLOR[3], .05, "A standard looking office area with a couple of desks \n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[4], .05, "One desk at the back is particularly large and dishelved \n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[4], .05, "Next to it is another door to the storage room \n")
                sleep(.5)
                office_choice = input(
                    "What do you check? (\"Desk\" \"Storage\" \"Garage\" ")
                while office_choice.lower() != "desk" and office_choice.lower() != "storage" and office_choice.lower() != "garage":
                    office_choice = input(
                        "What do you check? (\"Desk\" \"Storage\" ")
                if office_choice.lower() == "desk":
                    if self.car_key == True:
                        self.print_slow(self.COLOR[4], .05,
                                        "You feel your time would be better spent elsewhere \n")
                        sleep(.5)
                    else:
                        self.print_slow(
                            self.COLOR[3], .05, "Statements litter the surface of the desk \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[4], .05,
                                        "A locked case sits in the middle of the desk with a note on it \n")
                        sleep(.5)
                        read_note = input("Read the note? (y/n) \n")
                        while read_note != "y" and read_note != "n":
                            read_note = input("Read the note? (y/n) \n")
                        if read_note == "y":
                            self.print_slow(self.COLOR[3], .05,
                                            "\n\"\nI knew everyone was acting strange, bussiness has been chaotic as well. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "Those that could moved out from the bad image, but you'd think they had known something was up. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "I thought my employees were down from lack of bussiness, that's why they weren't talking as much. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "But they started saying weirder and weirder things, almost slurring, mashing, their words or thoughts together \n")
                            sleep(.5)
                            self.print_slow(
                                self.COLOR[1], .05, " - with each other! \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[1], .05,
                                            "I knew it was over when one of my own attacked me, I locked him in a car and the key inside this gun safe...\" \n")
                            sleep(.5)
                            self.print_slow(
                                self.COLOR[1], .05, "Think I'll need that going forward.\n\" \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[4], .05,
                                            "\n at the bottom a riddle reads: \"My code comes in order... \nI am the first, Those come after me, But anything else is last\n\" \n")
                            sleep(.5)
                        else:
                            self.print_slow(self.COLOR[3], .05,
                                            "Like a child on christmas you go straight for the box \n")
                            sleep(.5)
                        code_lock = input(
                            "A six digit code with numbers going 1 - 3 (ex: 123123)\n")
                        while code_lock != "121313":
                            code_lock = input(
                                "A six digit code with numbers going 1 - 3\n")
                        if code_lock == "121313":
                            self.print_slow(self.COLOR[0], .05,
                                            "The lock pops open revealing a car key inside! \n")
                            sleep(.5)
                            self.car_key = True
                            if self.car_encounter == True:
                                self.print_slow(self.COLOR[4], .05,
                                                "Looks like this will let me get the socket wrench \n")
                                sleep(.5)
                            else:  # doesn't know of encounter
                                self.print_slow(self.COLOR[1], .05,
                                                "Sure wouldn't want to meet whoever's locked in the car \n")
                                sleep(.5)
                elif office_choice.lower() == "storage":
                    if self.crowbar == True:
                        self.print_slow(self.COLOR[4], .05,
                                        "You feel you time would be better spent elsewhere \n")
                        sleep(.5)
                        continue
                    else:
                        self.storage()
                        stay = False
                        return
                elif office_choice.lower() == "garage":
                    self.garage()
                    return
            elif self.flash_light == False:
                self.print_slow(self.COLOR[3], .05,
                                "... the silence is deafening \n")
                sleep(.5)
                self.print_slow(self.COLOR[4], .05,
                                "a backup pack powering a small lamp illuminates a large desk in the back \n")
                sleep(.5)
                self.print_slow(self.COLOR[4], .05,
                                "as you walk towards it you notice a door with the word: \"Storage\"  \n")
                sleep(.5)
                office_choice = input(
                    "What do you check? (\"Desk\" \"Storage\" \"Garage\") \n")
                while office_choice.lower() != "desk" and office_choice.lower() != "storage" and office_choice.lower() != "garage":
                    office_choice = input(
                        "What do you check? (\"Desk\" \"Storage\" \"Garage\") \n")
                if office_choice.lower() == "desk":
                    if self.car_key == True:
                        self.print_slow(self.COLOR[4], .05,
                                        "You feel your time would be better spent elsewhere \n")
                        sleep(.5)
                    else:
                        self.print_slow(
                            self.COLOR[3], .05, "Statements litter the surface of the desk \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[4], .05,
                                        "A locked case sits in the middle of the desk with a note on it \n")
                        sleep(.5)
                        read_note = input("Read the note? (y/n) \n")
                        while read_note != "y" and read_note != "n":
                            read_note = input("Read the note? (y/n) \n")
                        if read_note == "y":
                            self.print_slow(self.COLOR[3], .05,
                                            "\n\"I knew everyone was acting strange, bussiness has been chaotic as well. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "Those that could, moved out from the bad image, but you'd think they had known something was up. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "I thought my employees were down from lack of bussiness, that's why they weren't talking as much. \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "But they started saying weirder and weirder things, almost slurring, mashing, their words or thoughts together \n")
                            sleep(.5)
                            self.print_slow(
                                self.COLOR[1], .05, " - with each other!")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "I knew it was over when one of my own attacked me, I locked him in a car and the key inside this gun safe.. \n")
                            sleep(.5)
                            self.print_slow(
                                self.COLOR[3], .05, "Think I'll need that going forward.\" \n")
                            sleep(.5)
                            self.print_slow(self.COLOR[3], .05,
                                            "\n at the bottom a riddle reads: \"My code comes in order... \nI am the first, Those come after me, But anything else is last\n")
                            sleep(.5)
                        else:
                            self.print_slow(self.COLOR[3], .05,
                                            "Like a child on christmas you go straight for the box \n")
                            sleep(.5)
                        code_lock = input(
                            "A six digit code with numbers going 1 - 3 (ex: 123123)\n")
                        while code_lock != "121313":
                            code_lock = input(
                                "A six digit code with numbers going 1 - 3\n")
                        if code_lock == "121313":
                            self.print_slow(self.COLOR[0], .05,
                                            "The lock pops open revealing a car key inside! \n")
                            sleep(.5)
                            self.car_key = True
                            if self.car_encounter == True:
                                self.print_slow(self.COLOR[3], .05,
                                                "Looks like this will let me get the socket wrench \n")
                                sleep(.5)
                            else:  # doesn't know of encounter
                                self.print_slow(self.COLOR[1], .05,
                                                "Surely wouldn't want to meet whoever's locked in the car \n")
                                sleep(.5)
                elif office_choice.lower() == "storage":
                    if self.crowbar == True:
                        self.print_slow(self.COLOR[4], .05,
                                        "You feel you time would be better spent elsewhere \n")
                        sleep(.5)
                        continue
                    else:
                        self.storage()
                        stay = False
                        return
                elif office_choice.lower() == "garage":
                    self.garage()
                    return

    def storage(self):
        while self.crowbar == False:
            if self.flash_light == True:
                self.print_slow(self.COLOR[3], .05,
                                "The storage room, or what's left of it, has been cleared out in a hurry \n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[3], .05, "In the corner a soft relfection catches your odds \n")
                sleep(.5)
                self.print_slow(self.COLOR[4], .05,
                                "It appears to be a crowbar \n")
                sleep(.5)
                take_crowbar = input("\ntake the crowbar? (y/n) \n")
                while take_crowbar != "y" and take_crowbar != "n":
                    take_crowbar = input("\ntake the crowbar? (y/n) \n")
                if take_crowbar == "y":
                    if self.car_encounter == True:
                        self.print_slow(
                            self.COLOR[3], .05, "Looks like this will hold whatever that was back \n")
                        sleep(.5)
                        self.crowbar = True
                        room_choice = input(
                            "What do you explore? (\"office\" \"garage\") \n")
                        while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                            room_choice = input(
                                "What do you explore? (\"office\" \"storage\") \n")
                        if room_choice.lower() == "office":
                            self.office()
                            return
                        elif room_choice.lower() == "garage":
                            self.garage()
                            return
                    else:
                        self.print_slow(self.COLOR[0], .05,
                                        "A handy tool, or weapon, depending on which half of life you're in \n")
                        sleep(.5)
                        self.crowbar = True
                        room_choice = input(
                            "What do you explore? (\"office\" \"garage\") \n")
                        while room_choice.lower() != "garage" and room_choice.lower() != "office" and room_choice.lower() != "storage":
                            room_choice = input(
                                "What do you explore? (\"office\" \"storage\") \n")
                        if room_choice.lower() == "office":
                            self.office()
                            return
                        elif room_choice.lower() == "garage":
                            self.garage()
                            return

            elif self.flash_light == False:
                self.print_slow(
                    self.COLOR[3], .1, "You swing the door open and wait . . . \n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[3], .05, "... not a sound, you take a step in \n")
                sleep(.5)
                self.print_slow(self.COLOR[1], .005, """
                    !#!#!#!#!#!#!
                    !#! CRASH !#!
                    !#!#!#!#!#!#!
                     \n""")
                sleep(.5)
                self.print_slow(
                    self.COLOR[1], .05, "Disheveled racks clutters you path causing a calamity  \n")
                sleep(.5)
                print(". \n")
                self.print_slow(self.COLOR[3], .05, ". . \n")
                sleep(.5)
                self.print_slow(self.COLOR[1], .005, """
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                     \n""")
                sleep(.5)
                self.print_slow(self.COLOR[1], .005,
                                "SOMETHING FROM THE LEFT CORNER OF THE ROOM DIDN'T WANT TO BE DISTURBED  \n")
                sleep(.5)
                self.print_slow(
                    self.COLOR[3], .05, "You panic and hurry to the other side of the room \n")
                sleep(.5)
                self.print_slow(self.COLOR[3], .05,
                                "As you maneuvur around debris you feel cold metal and hear a clang  \n")
                sleep(.5)
                self.print_slow(self.COLOR[4], .05,
                                "You're not sure what it is but any metal rod could be good right now \n")
                sleep(.5)
                take_crowbar = input("Take the metal rod? (y/n) ")
                while take_crowbar.lower() != "y" and take_crowbar.lower() != "n":
                    take_crowbar = input("Take the metal rod? (y/n) ")
                if take_crowbar == "y":
                    self.crowbar = True
                    self.print_slow(self.COLOR[3], .05,
                                    "You pick the bar up with relative ease, sliding it into your grip you feel a large hooking end  \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[3], .05,
                                    "A crowbar? Whatever - you reach the end of the room, bumping into the wall \n")
                    sleep(.5)
                    self.print_slow(
                        self.COLOR[0], .05, "... it's not a wall but a door! \n")
                    sleep(.5)
                    fof = input("(\"fight\" \"flight\" ")
                    while fof.lower() != "fight" and fof.lower() != "flight":
                        fof = input("(\"fight\" \"flight\" ")
                    if fof.lower() == "fight":
                        self.print_slow(self.COLOR[3], .05,
                                        "adrenaline courses through your viens - whatever that is sounds like its where you entered (across the room)  \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[3], .05,
                                        "eyes now somewhat adjusted can just barely make out some movement \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[3], .05, "you take a swing when you feel the time is right \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[1], .05,
                                        "THE HOOK OF YOUR CROWBAR GETS CAUGHT ON A ROUGE SHELF MID SWING - WHO PUT THAT THERE??  \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[3], .05, "YOU SWING WITH ALL YOU MIGHT REGARDLESS -  \n")
                        sleep(.5)
                        self.print_slow(self.COLOR[3], .05,
                                        "THE SHELF COMES TOPPLING DOWN IN FRONT OF YOU, HAVING A KNOCK ON AFFECT \n")
                        sleep(.5)
                        self.print_slow(
                            self.COLOR[1], .05, ". . . the sounds of struggle can be heard under the rubble . . . \n")
                        sleep(.5)
                    elif fof.lower() == "flight":
                        self.print_slow(self.COLOR[3], .05,
                                        "a coward doesn't fight... but they do live another day \n")
                        sleep(.5)

                elif take_crowbar == "n":  # you're not taking the crowbar?
                    self.print_slow(self.COLOR[3], .05,
                                    "You're done with the madness... frozen by your fears you stand still \n")
                    sleep(.5)
                    self.print_slow(self.COLOR[1], .005, """
                    CRUNCH !#!#!#!#!#
                    !#!#! CHOMP !#!#!
                    !#!#!#!#!#! CRACK
                     \n""")
                    sleep(.5)
                    self.life = False
                    self.end()
            if self.crowbar == False:
                self.print_slow(
                    self.COLOR[4], .05, "You feel like you're missing something . . . \n")
                sleep(.5)
                continue
            elif self.crowbar == True:
                self.print_slow(
                    self.COLOR[3], .05, "You decide to leave the storage room \n")
                sleep(.5)
                break
        # LEAVE OPTIONS
        # have everything to leave and know encounter
        if self.crowbar == True and self.car_key == True and self.car_encounter == True:
            self.print_slow(
                self.COLOR[4], .05, "You feel ready to get the socket wrench \n")
            sleep(.5)
            leave_storage = input("Head to the garage again? (y/n) \n")
            while leave_storage.lower() != "y" and leave_storage.lower() != "n":
                leave_storage = input("Head into garage again? (y/n) \n")
            if leave_storage.lower() == "n":
                self.print_slow(self.COLOR[3], .05,
                                "You tell yourself you don't want to go, but you have to... you must \n")
                sleep(.5)
                self.check_car()

            if leave_storage.lower() == "y":
                self.print_slow(self.COLOR[3], .05,
                                "You muster up your courage and head for the encounter once again \n")
                sleep(.5)
                self.check_car()

        # have everything but no encounter
        elif self.crowbar == True and self.car_key == True:
            self.print_slow(
                self.COLOR[3], .05, "You now have the means to open a car by choice, or force \n")
            sleep(.5)
            leave_storage = input("Head back to the garage? (y/n) \n")
            while leave_storage.lower() != "y" and leave_storage.lower() != "n":
                leave_storage = input("Head back to the garage? (y/n) \n")
            if leave_storage.lower() == "y":
                self.print_slow(self.COLOR[3], .05,
                                "You enter the garage door \n")
                sleep(.5)
                self.check_car()

            elif leave_storage.lower() == "n":
                self.print_slow(self.COLOR[3], .05,
                                "You have no idea where to go, but the garage is the only mystery left \n")
                sleep(.5)
                self.check_car()

        # knows encounter but no keys
        elif self.car_encounter == True:
            self.print_slow(self.COLOR[1], .05,
                            "The fear still grips you... \n")
            sleep(.5)
            leave_storage = input("\"office\" \"garage\" ")
            if leave_storage == "office":
                self.office()

            else:  # leave_storage == "garage"
                you_sure = input(
                    "I'm glad that thing is locked in the car\n \"office\" \"garage\" ")
                if you_sure.lower() == "office":
                    self.office()

                else:
                    self.garage()

    def end(self):
        if self.socket_wrench == True:
            self.print_slow(self.COLOR[0], .05,
                            "You grab a tire that looks like it will fit your car and leave the garage \n")
            sleep(.5)
            self.key += 1
            self.win = True
            return
    # test to make sure class works

    def play_room_three(self):
        choice = input("Would you like to get another key? (y/n)")

        if choice.lower() == "y":
            # print(f"RM3: You had {self.key} keys before")
            self.key += 1
            return {"key": self.key, "life": self.life}

        else:
            print("You died")
            self.life = False
            return {"key": self.key, "life": self.life}

            pass
            # print(f"RM3: You have {self.key} keys")
            # return self self.key

            # test = Garage(key=1)
            # test.play_garage()
