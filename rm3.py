# Jake's room - Mechanics garage
# Goal: Obtain fresh Tire
# - Tire: Obtain Socket Wrench
# -- Socket wrench: Locked inside car with zombie
# --- Car key: Riddle from accounting
# --- Crowbar: Found in storage
# -- No crowbar? 50% chance of death
# -- Crowbar? Hold zombie back and grab socket wrench

from time import sleep


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

    def test_garage(self):
        print("you enter the garage")
        print("as if the scenery is enough, the smell of blood lingers in the air")
        print("you spot a key with a note propped up near it on a counter")
        test_input = input("Would you you like a key? (y/n)\n ")

        if test_input.lower() == "y":
            print(
                "you graciously accept the key, thankful for the hardwork and blood shed to get it here")
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
        print(
            "You enter the garage, the lights appear to be out but the store front windows allow you to see")
        sleep(.5)
        print(
            "You walk up to the counter and peak around . . . No one seems to be aronud")
        sleep(.5)
        print("As you scan the room you spot a door labeled \"Garage\" and what could be supplies littered behind the counter")
        scan_entrance = input(
            "What do you check? (\"counter\" or \"garage\") \n")
        while scan_entrance.lower() != "counter" and scan_entrance.lower() != "garage" and scan_entrance.lower() != "t":
            scan_entrance = input(
                "Invalid input - What do you check? (\"counter\" or \"garage\") \n")
        if scan_entrance.lower() == "t":
            self.check_car()
        elif scan_entrance.lower() == "counter":
            print(
                "You see a flashlight and batteries behind the counter... almost like someone dropped them")
            take_light = input("Take the flashlight? (y/n) : ")

            while take_light.lower() != "y" and take_light.lower() != "n":
                take_light = input(
                    "Invalid input - Take the flashlight? (y/n) : ")

            if take_light.lower() == "y":
                print("You step behind the counter and pick up the flashlight")
                self.flash_light = True
                print(
                    "You turn the light on to verify that it works . . . it does!")
                sleep(.5)
                print(
                    "But you spot the flash lights reflection on a pool of some viscous liquid")
                sleep(.5)
                print("... it's probablt oil . . . hopefully")
                sleep(.8)
                print(
                    "With a flashlight equipped you feel ready to enter the garage")
                sleep(1)

            else:  # take_light == n
                print(
                    "A bold and brash adventurer like you don't need no damn lights")
        elif scan_entrance.lower() == "garage":  # scan_entrance == garage
            print("With no fear, you plunge yourself into the dark garage")
            self.garage_intro()

        # after counter
        if self.flash_light == True:
            print("You use flashlight to help you see in the large garage")
            self.garage_intro()

        else:  # scan_entrance == garage
            print("With no fear, you plunge yourself into the dark garage")
            self.garage_intro()

    def garage_intro(self):
        if self.flash_light == True:
            print("You open the door to the garage")
            sleep(.5)
            print("Thankfully you have a flashlight and can look around")
            print(
                "As you scan the room with light you think you hear the sound of shuffling... but it quickly dies down...")
            sleep(.5)
            print(
                "The garage seems to be a large working area for mechanics with doors to various rooms")
            sleep(.5)
            print(
                "Using your flaslight you find the doors are clearly labeled \n\"Entrance\" \"Office\" \"Storage\" ")
        else:
            print("The garage is dark without a flashlight")
            print("You grope around the walls hoping to find a door...")
            print(". . . you hear a small crash as something dropped in the garage")
            print("the sounds of someone struggling can be heard...")
            print(
                "you come to a junction of doors... in the limited visibility you make out the words")
            print("\n\"Entrance\" \"Office\" \"Storage\"")
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
                    print(
                        "You walk around the garage, it feels as if life suddenly stopped...")
                    print(
                        "Cars are still lifted to be worked on, the occasional oil puddle is present... but nothing looks put away...")
                    print(
                        "A tire pile! You approach hoping to find a replacement for your car")
                    print(
                        ". . . tires... but no wrench to install them... better keep looking")
                    self.check_car()
                    return

                else:  # flash_light == False
                    print(
                        "You hug the outside wall of the garage... You hear strange sounds coming from it's large rolling doors")
                    print(
                        "The sound of a struggle is growing louder as you creep to the back of the garage")
                    print("""
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    !! You tumble over something !!
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    """)
                    print(". . . Tires!?")
                    print(
                        "You feel a large pile of tires in front of you! The bolts are locked in")
                    print("I should find some kind of wrench")
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
            print("You utter a greeting to the void")
            print(". . . h . e . l . l . o . .")
            return

    def check_car(self):
        if self.car_encounter == False:
            if self.flash_light == True:
                if self.car_key == False:
                    print(
                        "you spot a lowered car with tools scattered around it, maybe I'll find a wrench there")
                    print(
                        "nothing of use appears to be on the ground, you try to open the car but it's locked")
                    print(
                        "peering in with eyes cupped to the window & flashing held up you look inside")
                    print(
                        "A socket wrench on the seat! The door is locked, I should find a key-")
                    print("""
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    """)
                    print("SOMETHING LEAPS AT YOU FROM INSIDE THE CAR")
                    print("... it's blocked by the window but continues to struggle")
                    print("a strange fluid coats the inside of the window")
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
                        print(
                            "Without a weapon you tap the glass on the opposite side to get the creatures attention")
                        print(
                            "running to the other side you rush to unlock the door and get the wrench")
                        self.socket_wrench = True
                        print("You get the wrench, but not unscathed")
                        self.end()
                    elif self.crowbar == True:
                        print(
                            "You unlock the door... crowbar in hand ready for whatever comes at you")
                        print("... it's ... smiling at you?")
                        print("The creature leaps at you!")
                        print(
                            "but the crowbar prevents it from reaching you or blocking your path the the socket wrench")
                        print(
                            "You take the wrench, slam the door and bolt away from the car")
                        self.socket_wrench = True
                        self.end()
            elif self.flash_light == False:
                if self.car_key == False:
                    print(
                        "you bump into a lowered car with tools scattered around it, maybe I'll find a wrench around you")
                    print(
                        "nothing of use appears to be on the ground, you try to open the car but it's locked")
                    print(
                        "peering in with eyes cupped to the window")
                    print(
                        "as your eyes adjust you see a socket wrench on the seat! I should find a key-")
                    print("""
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    """)
                    print("SOMETHING LEAPS AT YOU FROM INSIDE THE CAR")
                    print(
                        "... it's blocked by the window but continues to struggle")
                    print("a strange fluid coats the inside of the window")
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
                        print(
                            "Without a weapon you tap the glass on the opposite side to get the creatures attention")
                        print(
                            "running to the other side you rush to unlock the door and get the wrench")
                        self.socket_wrench = True
                        print("You get the wrench, but not unscathed")
                        self.end()
                    elif self.crowbar == True:
                        print(
                            "You unlock the door... crowbar in hand ready for whatever comes at you")
                        print("... it's ... smiling at you?")
                        print("The creature leaps at you!")
                        print(
                            "but the crowbar prevents it from reaching you or blocking your path the the socket wrench")
                        print(
                            "You take the wrench, slam the door and bolt away from the car")
                        self.socket_wrench = True
                        self.end()
        elif self.car_encounter == True:
            if self.flash_light == True:
                if self.car_key == True:
                    if self.crowbar == True:
                        print(
                            "You approach the sounds of struggle, muffled behind car windows")
                        print(
                            "you insert the car key into the door... The beast makes a noise as if it knowns")
                        print(
                            "You rip the door open, shove the crowbar in, feeling the weight of the beast trying to jump at you")
                        print(
                            "With the beast held back you grab the socket wrench, slam the door closed and hope to never experience that again")
                        self.socket_wrench = True
                        self.end()
                    elif self.crowbar == False:
                        print(
                            "You approach the sounds of struggle, muffled behind car windows")
                        print(
                            "you insert the car key into the door... The beast makes a noise as if it knows")
                        print(
                            "You rip the door open, and leap for the wrench before the beast can get to you")
                        self.socket_wrench = True
                        print("You get the wrench, but not unscathed")
                        self.end()
                elif self.car_key == False:
                    print("I don't have the key to unlock the car")
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
                        print(
                            "You approach the sounds of struggle, muffled behind car windows")
                        print(
                            "you insert the car key into the door... The beast makes a noise as if it knowns")
                        print(
                            "You rip the door open, shove the crowbar in, feeling the weight of the beast trying to jump at you")
                        print(
                            "With the beast held back you grab the socket wrench, slam the door closed and hope to never experience that again")
                        self.socket_wrench = True
                        self.end()
                    elif self.crowbar == False:
                        print(
                            "You approach the sounds of struggle, muffled behind car windows")
                        print(
                            "you insert the car key into the door... The beast makes a noise as if it knows")
                        print(
                            "You rip the door open, and leap for the wrench before the beast can get to you")
                        self.socket_wrench = True
                        print("You get the wrench, but not unscathed")
                        self.end()
                elif self.car_key == False:
                    print("I don't have the key to unlock the car")
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
                print("A standard looking office area with a couple of desks")
                print("One desk at the back is particularly large and dishelved")
                print("Next to it is another door to the storage room")
                office_choice = input(
                    "What do you check? (\"Desk\" \"Storage\" \"Garage\" ")
                while office_choice.lower() != "desk" and office_choice.lower() != "storage" and office_choice.lower() != "garage":
                    office_choice = input(
                        "What do you check? (\"Desk\" \"Storage\" ")
                if office_choice.lower() == "desk":
                    if self.car_key == True:
                        print(
                            "You feel your time would be better spent elsewhere")
                    else:
                        print("Statements litter the surface of the desk")
                        print(
                            "A locked case sits in the middle of the desk with a note on it")
                        read_note = input("Read the note? (y/n) \n")
                        while read_note != "y" and read_note != "n":
                            read_note = input("Read the note? (y/n) \n")
                        if read_note == "y":
                            print(
                                "\n\"\nI knew everyone was acting strange, bussiness has been chaotic as well.")
                            print(
                                "Those that could moved out from the bad image, but you'd think they had known something was up.")
                            print(
                                "I thought my employees were down from lack of bussiness, that's why they weren't talking as much.")
                            print(
                                "But they started saying weirder and weirder things, almost slurring, mashing, their words or thoughts together - with each other!")
                            print(
                                "I knew it was over when one of my own attacked me, I locked him in a car and the key inside this gun safe...")
                            print("Think I'll need that going forward.\n\"")
                            print(
                                "\n at the bottom a riddle reads: \"My code comes in order... \nI am the first, Those come after me, But anything else is last\n")
                        else:
                            print(
                                "Like a child on christmas you go straight for the box")
                        code_lock = input(
                            "A six digit code with numbers going 1 - 5 (ex: 123451)\n")
                        while code_lock != "121313":
                            code_lock = input(
                                "A six digit code with numbers going 1 - 5\n")
                        if code_lock == "121313":
                            print(
                                "The lock pops open revealing a car key inside!")
                            self.car_key = True
                            if self.car_encounter == True:
                                print(
                                    "Looks like this will let me get the socket wrench")
                            else:  # doesn't know of encounter
                                print(
                                    "Sure wouldn't want to meet whoever's locked in the car")
                elif office_choice.lower() == "storage":
                    if self.crowbar == True:
                        print(
                            "You feel you time would be better spent elsewhere")
                        continue
                    else:
                        self.storage()
                        stay = False
                        return
                elif office_choice.lower() == "garage":
                    self.garage()
                    return
            elif self.flash_light == False:
                print("... the silence is deafening")
                print(
                    "a backup pack powering a small lamp illuminates a large desk in the back")
                print(
                    "as you walk towards it you notice a door with the word: \"Storage\" ")
                office_choice = input(
                    "What do you check? (\"Desk\" \"Storage\" \"Garage\") \n")
                while office_choice.lower() != "desk" and office_choice.lower() != "storage" and office_choice.lower() != "garage":
                    office_choice = input(
                        "What do you check? (\"Desk\" \"Storage\" \"Garage\") \n")
                if office_choice.lower() == "desk":
                    if self.car_key == True:
                        print(
                            "You feel your time would be better spent elsewhere")
                    else:
                        print("Statements litter the surface of the desk")
                        print(
                            "A locked case sits in the middle of the desk with a note on it")
                        read_note = input("Read the note? (y/n) \n")
                        while read_note != "y" and read_note != "n":
                            read_note = input("Read the note? (y/n) \n")
                        if read_note == "y":
                            print(
                                "\n\"I knew everyone was acting strange, bussiness has been chaotic as well.")
                            print(
                                "Those that could moved out from the bad image, but you'd think they had known something was up.")
                            print(
                                "I thought my employees were down from lack of bussiness, that's why they weren't talking as much.")
                            print(
                                "But they started saying weirder and weirder things, almost slurring, mashing, their words or thoughts together - with each other!")
                            print(
                                "I knew it was over when one of my own attacked me, I locked him in a car and the key inside this gun safe...")
                            print("Think I'll need that going forward.\"")
                            print(
                                "\n at the bottom a riddle reads: \"My code comes in order... \nI am the first, Those come after me, But anything else is last\n")
                        else:
                            print(
                                "Like a child on christmas you go straight for the box")
                        code_lock = input(
                            "A six digit code with numbers going 1 - 5 (ex: 123451)\n")
                        while code_lock != "121313":
                            code_lock = input(
                                "A six digit code with numbers going 1 - 5\n")
                        if code_lock == "121313":
                            print(
                                "The lock pops open revealing a car key inside!")
                            self.car_key = True
                            if self.car_encounter == True:
                                print(
                                    "Looks like this will let me get the socket wrench")
                            else:  # doesn't know of encounter
                                print(
                                    "Surely wouldn't want to meet whoever's locked in the car")
                elif office_choice.lower() == "storage":
                    if self.crowbar == True:
                        print(
                            "You feel you time would be better spent elsewhere")
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
                print(
                    "The storage room, or what's left of it, has been cleared out in a hurry")
                print("In the corner a soft relfection catches your odds")
                print("It appears to be a crowbar")
                take_crowbar = input("\ntake the crowbar? (y/n) \n")
                while take_crowbar != "y" and take_crowbar != "n":
                    take_crowbar = input("\ntake the crowbar? (y/n) \n")
                if take_crowbar == "y":
                    if self.car_encounter == True:
                        print("Looks like this will hold whatever that was back")
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
                        print(
                            "A handy tool, or weapon, depending on which half of life you're in")
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
                print("You swing the door open and wait . . .")
                print("... not a sound, you take a step in")
                print("""
                    !#!#!#!#!#!#!
                    !#! CRASH !#!
                    !#!#!#!#!#!#!
                    """)
                print("Disheveled racks clutters you path causing a calamity ")
                print(".")
                print(". .")
                print("""
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    !@# RRRWAAAAAUURRRGG !@#
                    !@#!@#!@#!@#!@#!@#!@#!@#
                    """)
                print(
                    "SOMETHING FROM THE LEFT CORNER OF THE ROOM DIDN'T WANT TO BE DISTURBED ")
                print("You panic and hurry to the other side of the room")
                print(
                    "As you maneuvur over the rubble you feel cold metal and hear a clang ")
                print(
                    "You're not sure what it is but any metal rod could be good right now")
                take_crowbar = input("Take the metal rod? (y/n) ")
                while take_crowbar.lower() != "y" and take_crowbar.lower() != "n":
                    take_crowbar = input("Take the metal rod? (y/n) ")
                if take_crowbar == "y":
                    self.crowbar = True
                    print(
                        "You pick the bar up with relative ease, sliding your hands to get a grip you feel a large hooking end ")
                    print(
                        "A crowbar? Whatever - you reach the end of the room, bumping into the wall")
                    print("... it's not a wall but a door!")
                    fof = input("(\"fight\" \"flight\" ")
                    while fof.lower() != "fight" and fof.lower() != "flight":
                        fof = input("(\"fight\" \"flight\" ")
                    if fof.lower() == "fight":
                        print(
                            "adrenaline courses through your viens - whatever that is sounds like its where you entered (across the room) ")
                        print(
                            "eyes now somewhat adjusted can just barely make out some movent")
                        print("you take a swing when you feel the time is right")
                        print(
                            "THE HOOK OF YOUR CROWBAR GETS CAUGHT ON A ROUGE SHELF MID SWING - WHO PUT THAT THERE?? ")
                        print("YOU SWING WITH ALL YOU MIGHT REGARDLESS - ")
                        print(
                            "THE SHELF COMES TOPPLING DOWN IN FRONT OF YOU, HAVING A KNOCK ON AFFECT")
                        print(". . . the sounds of struggle can be heard . . .")
                    elif fof.lower() == "flight":
                        print(
                            "a coward doesn't fight... but they do live another day")

                elif take_crowbar == "n":  # you're not taking the crowbar?
                    print(
                        "You're done with the madness... frozen by your fears you stand still")
                    print("""
                    CRUNCH !#!#!#!#!#
                    !#!#! CHOMP !#!#!
                    !#!#!#!#!#! CRACK 
                    """)
                    self.life = False
                    self.end()
            if self.crowbar == False:
                print("You feel like you're missing something . . .")
                continue
            elif self.crowbar == True:
                print("You decide to leave the storage room")
                break
        # LEAVE OPTIONS
        # have everything to leave and know encounter
        if self.crowbar == True and self.car_key == True and self.car_encounter == True:
            print("You feel ready to get the socket wrench")
            leave_storage = input("Head to the garage again? (y/n) \n")
            while leave_storage.lower() != "y" and leave_storage.lower() != "n":
                leave_storage = input("Head into garage again? (y/n) \n")
            if leave_storage.lower() == "n":
                print(
                    "You tell yourself you don't want to go, but you have to... you must")
                self.check_car()

            if leave_storage.lower() == "y":
                print(
                    "You muster up your courage and head for the encounter once again")
                self.check_car()

        # have everything but no encounter
        elif self.crowbar == True and self.car_key == True:
            print("You now have the means to open a car by choice, or force")
            leave_storage = input("Head back to the garage? (y/n) \n")
            while leave_storage.lower() != "y" and leave_storage.lower() != "n":
                leave_storage = input("Head back to the garage? (y/n) \n")
            if leave_storage.lower() == "y":
                print("You enter the garage door")
                self.check_car()

            elif leave_storage.lower() == "n":
                print(
                    "You have no idea where to go, but the garage is the only mystery left")
                self.check_car()

        # knows encounter but no keys
        elif self.car_encounter == True:
            print("The fear still grips you...")
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
            print(
                "You grab a tire that looks like it will fit your car and leave the garage")
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
