# Clinic storyline
# Goal - find meds and bandages
# Challenges:
# - collect items:
# - clinic key - it's in an office
# to get into the office, player needs to find screw driver and hammer to get into clinic office
# survivor Dr Stephen Baker is alive and hurt. He's been stabbed by his nurse in his side.
# the doctor put you on a quest to get a trauma kit in an exam room.
# two nurses are in the builiding last he recalls. He is not sure where they are

# side lore - listen to the voice mail machine in the

# - potential items to get:
# items in maintenance closet
# iron pipe
# hammer
# screw driver


class rm1_class:
    def __init__(self, main):
        self.key = main.key
        self.life = main.life
        self.clinic_key = False
        self.screwdriver = False
        self.lighter = False

        # key passed in from Main_Game creating new rm1_class
  # this initializes the game

    def play_room_one(self):
        print("Would you like to enter the clinic?")
        print("Choose yes or no: ", end="")
        choice = input()
        if choice == "yes":
            print("\n You enter the lobby of the clinic. You are looking for gauze to wrap your head wound and some pain killers \n")
            self.play_lobby()

        else:
            # if no, send player to main.py file play_main function
            pass

    # You enter the lobby

    def play_lobby(self):
        print("\n The lights are off. The lobby looks like a mess. Some chairs have been thrown about and a waste toppled over. There is a receptionist desk connected to the lobby, and a door into the clinic on your right. The office doesn't seem to be accessible from the lobby.")
        print("Check door or desk?: ", end="")
        choice = input()
        if choice.lower() == "door":
            print(
                "\n You go to the door, It's locked. You need to find a key or maybe pick the lock?")
            print("Do you want to try to open the door?", end="")
            choice = input()
            if self.clinic_key == True:
                print("You opened the clinic door \n")
                self.clinic_hallway()

            else:
                print(
                    "You don't have a key or a way to pick the lock yet. You turn around.")
                self.play_lobby()

        if choice.lower() == "desk":
            print(
                "You go stand in front of the receptionist desk. You could climb over and search the office.")
            print("Do you climb over? yes or no?: ", end="")
            choice = input()

            if choice.lower() == "yes":
                self.play_clinic_front_office()

            else:
                choice.lower() == "no"
                print("You turn around.")
                self.play_lobby()

    # office scene

    def play_clinic_front_office(self):
        print("You climb ontop of the desk. The office is dimly lit and what little light you see is coming from the mostly closed blinds on the walls. The office looks messy and there are signs of a struggle. There is a door connecting the office to the hallway on your right")
        # choice
        print("look around or open blinds?", end="")
        choice = input()
        if choice == "look around":
            print(
                "Its very dark. You can't make out much... maybe you could find a candle or open the blinds")
            self.clinic_front_office_dark()
        else:
            print("You make your way to the wall and open the blinds. Light floods the room. You can see things clearly now")
            self.clinic_front_office_light()

    def clinic_front_office_dark(self):
        print("As you look around the office you bump into one of the desks. A small desk lamp falls and hits the floor with a thud. Hopefully no one heard")
        # choice
        print("Would you like to search the desks or investigate room?", end="")
        choice = input()

        # choice - search office desks
        if choice == "search desks":
            print(
                "There are two desks in the office. The receptionist desk and the nurses desk.")

            print(
                "Which would you like to search? receptionist desk or nurses desk?", end="")
            if choice == "receptionist desk":
                print("You searched the receptionist desk. You find a lighter!")
                self.lighter = True
                self.clinic_front_office_dark()
            if choice == "nurse desk":
                print(
                    "You search the nurses desk. You find a key to the clinic lobby door!")
                print("You hear the creeking of a door opening near you...")
                self.clinic_key = True
                self.clinic_front_office_dark()
        else:

            # choice - investigate room- dark

            if choice == "investigate room":
                #
                #
                # create exit conditions due to death
                #
                #
                while self.life == True:
                    print(
                        "You start to move around the dimly lit room. You notice the office door slowly opens and a nurse looks at you. In the darkness is a figure staring at you. After a second, you notice it's a nurse.")
                    print(
                        "Ask her for help? Yes or no:", end="")
                    choice = input()
                    if choice == "yes":
                        print(
                            "You step forward excitingly toward her for help and before you can ask a question")
                        print("The nurse lunges at you. She closes the distance between you two at an alarming rate. Before you can even react she sticks a syringe in your chest and starts laughing. You have been injected with a heavy sedative. You died.")
                        self.life = False
                        break
                    if choice == "no":
                        print("You hesitate and take a step backwards. Something feels off about the nurse. She notices you and starts sprinting at a full pace towards you. You turn to jump over the receptionist desk but she catches you by the collar of your shirt. She stabs a syringe into your neck and starts laughing. You have been in injeced with a heavy sedative. You died.")
                        self.life = False
                        break

    def clinic_front_office_light(self):
        print("As you look around you notice signs of a struggle and a blood stain on the carpet.")
        print("Would you like to search the desks or the office? Choose office or desks:", end="")
        choice = input()
        if choice == "search desks":
            print(
                "There are two desks in the office. The receptionist desk and the nurses desk.")

            print(
                "Which would you like to search? receptionist desk or nurses desk?", end="")
            if choice == "receptionist desk":
                print("You searched the receptionist desk. You find a lighter!")
                self.lighter = True
                self.clinic_front_office_light()
            if choice == "nurse desk":
                print(
                    "You search the nurses desk. You find a key to the clinic lobby door!")
                self.clinic_key = True
                self.clinic_front_office_light()
        else:
            if choice == "investigate":
                print("The office is a mess. There is blood on the ground near the office door. Patient records and memos strewn everywhere. Some sort of fight happened here. A newspaper article with a big red circle around ")
                print("")

    # def lookaround_office_front_desk(self):

    # #open blinds
    # if choice == "open blinds" or choice == "blinds":
    #     print("You open the blinds and light illuminates the room. The empty streets in front of you give you chills. Dark shadows recede and you can see the office more clearly. Chairs have been knocked over, a vase had been knocked over and shattered on the floor. Various papers are scattered around the floor.")
    #     print("The room layout consists of the front office desk for check in and check out. Two other desks in the center of the room for other nurses. Directly in front of you are filing cabinets ")

    #     def clinic_floor_lights_on(self):
    #         pass

    #     def clinic_floor_lights_off(self):
    #         pass
        # look around in dark

    def clinic_hallway(self):
        print("The hallway in front of you it pitch black.")

    # def test_room_one(self):
    #     choice = input("Would you like to get another key? (y/n)")
    #     print(f"You now have {self.key} keys")

    #     if choice.lower() == "y":
    #         # print(f"RM3: You had {self.key} keys before")
    #         self.key += 1
    #         return {"key": self.key, "life": self.life}

    #     else:
    #         print("You died")
    #         self.life = False
    #         return {"key": self.key, "life": self.life}

    #         pass

        # if choice.lower() == "desk":
        #     self.key += 1
        #     print(self.key)
        #     print("RM1: Yes? Jokes on you - you never had a choice")
        # else:
        #     print("RM1: NO!? Jokes on you - you never had a choice")


# remove the bottom test variables once you're done
# test_rm1 = rm1_class()
# test_rm1.play_room_one()
