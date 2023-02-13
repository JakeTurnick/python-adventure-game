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
        self.flashlight = False

        # key passed in from Main_Game creating new rm1_class
  # this initializes the game

    def play_room_one(self):
        print("Would you like to enter the clinic?")
        print("Enter 'yes' or 'no': ", end="")
        choice = input().lower()
        while choice not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no': ", end="")
            choice = input().lower()
        if choice == "yes":
            print("You enter the lobby of the clinic. You are looking for gauze to wrap your head wound and some pain killers \n")
            self.play_lobby()
        else:
            # if no, send player to main.py file play_main function
            pass

    # You enter the lobby

    def play_lobby(self):
        print("The lights are off. The lobby looks like a mess. Some chairs have been thrown about and a trash bin toppled over. There is a receptionist desk connected to the lobby, and a door into the clinic on your right. The office doesn't seem to be accessible from the lobby. \n")
        print("Enter 'door' or 'desk': ", end="")
        choice = input().lower()
        while choice not in ['door', 'desk']:
            print("Invalid input. Please enter 'door' or 'desk': ", end="")
            choice = input().lower()
        if choice == "door":
            print("You go to the door, It's locked. You need a key")
            print("Do you want to try to open the door? Enter 'yes' or 'no': ", end="")
            choice = input().lower()
            while choice not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no': ", end="")
                choice = input().lower()
            if self.clinic_key == True:
                print("You opened the clinic door \n")
                self.clinic_hallway()
            else:
                print(
                    "You don't have a key or a way to pick the lock yet. You turn around.\n")
                self.play_lobby()
        elif choice == "desk":
            print(
                "You go stand in front of the front desk. You could climb over and search the office. \n")
            print("Do you climb over? Enter 'yes' or 'no': ", end="")
            choice = input().lower()
            while choice not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no': ", end="")
                choice = input().lower()
            if choice == "yes":
                self.play_clinic_front_office()
            else:
                print("You turn around. \n")
                self.play_lobby()

    # office scene

    def play_clinic_front_office(self):
        print("You climb ontop of the desk. The office is dimly lit and what little light you see is coming from the mostly closed blinds on the walls. The office looks messy and there are signs of a struggle. There is a door connecting the office to the hallway on your right\n")
        # choice
        print("look around or open blinds? ", end="")
        while choice not in ['look around', 'open blinds']:
            print("Invalid input. Please enter 'look around' or 'open blinds': ", end="")
            choice = input().lower()
        if choice == "look around":
            print(
                "In the low light you can't make out much... maybe you could find a flashlight or open the blinds")
            self.clinic_front_office_dark()
        elif choice == "open blinds":
            print(
                "You make your way to the wall and open the blinds. Light floods the room. You can see things clearly now")
            self.clinic_front_office_light()

    def clinic_front_office_dark(self):
        print("As you look around the office you bump into one of the desks. A small desk lamp falls and hits the floor with a thud. Hopefully no one heard. You don't see much of interest.")
        # choice
        print(
            "Would you like to search the desks or the room? Choose desks or room: ", end="")
        while choice not in ['desks', 'room']:
            print("Invalid input: please choose 'desks' or 'room'", end="")
            choice = input().lower()

        # choice - search office desks
        if choice == "desks":
            print(
                "There are two desks in the office. The front desk and the nurses desk. \n")

            print(
                "Which would you like to search: front desk or nurses desk?", end="")
            while choice not in ['front desk', 'nurses desk']:
                print("Invalid input: please choose 'front desk' or 'nurses desk' ")
                choice = input().lower()
            if choice == "front desk":
                print("You searched the front desk. You find a flashlight!")
                self.flashlight = True
                self.clinic_front_office_dark()
            if choice == "nurse desk":
                print(
                    "You search the nurses desk. You find a key to the clinic lobby door!")
                print("You hear the creeking of a door opening near you... \n")
                self.clinic_key = True
                self.clinic_front_office_dark()
        elif choice == "room":

            # choice - investigate room- dark

            #
            #
            # create exit conditions due to death
            #
            #
            while self.life == True:
                print(
                    "You start to move around the dimly lit room. You notice the office door slowly opens and a nurse looks at you. In the darkness is a figure staring at you. After a second, you notice it's a nurse. \n")
                print(
                    "Ask her for help? Yes or no:", end="")
                while choice not in ['yes', 'no']:
                    choice = input().lower
                if choice == "yes":
                    print(
                        "You step forward excitingly toward her for help and before you can ask a question")
                    print("The nurse lunges at you. She closes the distance between you two at an alarming rate. Before you can even react she sticks a syringe in your chest and starts laughing. You have been injected with a heavy sedative. You died. \n")
                    self.life = False
                    break
                if choice == "no":
                    print("You hesitate and take a step backwards. Something feels off about the nurse. She notices you and starts sprinting at a full pace towards you. You turn to jump over the front desk but she catches you by the collar of your shirt. She stabs a syringe into your neck and starts laughing. You have been in injeced with a heavy sedative. You died. \n")
                    self.life = False
                    break

    def clinic_front_office_light(self):
        print("As you look around you notice signs of a struggle and a blood stain on the carpet. \n")
        print("Would you like to search the desks or the office? Choose office or desks:", end="")
        while choice not in ['office', 'desks']:
            print("Invalid input: please enter 'office' or 'desks'")
            choice = input()
        if choice == "desks":
            print(
                "There are two desks in the office. The front desk and the nurses desk. \n")

            print(
                "Which would you like to search: front or nurses desk? ", end="")
            choice = input()
            if choice == "front desk":
                print("You searched the front desk. You find a flashlight!")
                self.flashlight = True
                self.clinic_front_office_light()
            if choice == "nurse desk":
                print(
                    "You search the nurses desk. You find a key to the clinic lobby door! \n")
                self.clinic_key = True
                self.clinic_front_office_light()

        elif choice == "office":
            print("The office is a mess. There is blood on the ground near the office door. Patient records and memos strewn everywhere. Some sort of fight happened here. A newspaper article with a big red circle around ")

    def news_or_blood(self):
        print("investigate newspaper or blood? Or go back?", end="")
        choice = input()

        if choice == "newspaper":
            print("You see a newspaper titled, 'SCIENTIST MAKE BREAKTHROUGH DISCOVERY IN LOCAL LAB', circled in red with a note 'this is why i hear the whispers...... I AM NOT CRAZY!!! ITS THEM!'")
            self.news_or_blood()

        if choice == "blood":
            print("You find a pool of blood on the floor near the office door. It looks like someone was dragged into the door. Near the door you find a bloody screwdriver. You pick up the screwdriver.")
            self.screwdriver = True
            self.news_or_blood()

        if choice == "go back":
            self.front_desk()

    def front_desk(self):
        print("You are by the front desk. Jump over to the lobby or stay here? Choose lobby or stay", end="")
        choice = input()
        if choice == "lobby":
            self.play_lobby()

    def clinic_hallway(self):
        print("The hallway in front of you it pitch black. \n")

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
