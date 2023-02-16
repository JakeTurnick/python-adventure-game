# Clinic storyline
# Goal - find meds and bandages
# Challenges:
# - collect items:
# - clinic key - it's in an office
# to get into the office, player needs to find screw driver and hammer to get into clinic office
# the doctor put you on a quest to get a trauma kit in an exam room.
# two nurses are in the builiding last he recalls. He is not sure where they are

from time import sleep


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
            return {"key": self.key, "life": self.life}
        if choice == "no":
            self.back_to_main()
            return {"key": self.key, "life": self.life}
            # return
        # teting function currently takes you to the end of game.
        # else:
        # if no, send player to main.py file play_main function
        # pass
#
# trigger to take to test area: test area currently is the end of the game

#

    # def take_to_test(self):
    #     self.test_mark()
    # You enter the lobby

    def play_lobby(self):
        print("The lights are off. The lobby looks like a mess. Some chairs have been thrown about and a trash bin toppled over. There is a receptionist desk connected to the lobby, and a door into the clinic on your right. The office doesn't seem to be accessible from the lobby. \n")
        print("Enter 'door' or 'desk': ", end="")
        sleep(.1)
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
                print(
                    "You carefully crawl on top of the desk and make your way over. \n")
                self.play_clinic_front_office()
            else:
                print("You turn around. \n")
                self.play_lobby()

    # office scene

    def play_clinic_front_office(self):
        print("The office is dimly lit and what little light you see is coming from the mostly closed blinds on the walls. The office looks messy and there are signs of a struggle. There is a door connecting the office to the hallway on your right\n")
        print("look around or open blinds? ", end="")
        choice = input().lower()
        while choice not in ['look around', 'open blinds']:
            print("Invalid input. Please enter 'look around' or 'open blinds': ", end="")
            choice = input().lower()
        if choice == "look around":
            print(
                "In the low light you can't make out much... maybe you could find a flashlight or open the blinds")
            self.clinic_front_office_dark()
        if choice == "open blinds":
            print(
                "You make your way to the wall and open the blinds. Light floods the room. You can see things clearly now")
            self.clinic_front_office_light()

    def clinic_front_office_dark(self):
        print("As you look around the office you bump into one of the desks. A small desk lamp falls and hits the floor with a thud. Hopefully no one heard. You don't see much of interest.")
        # choice
        print(
            "Would you like to search the desks or the room? Choose desks or room: ", end="")
        choice = input().lower()
        while choice not in ['desks', 'room']:
            print("Invalid input: please choose 'desks' or 'room'", end="")
            choice = input().lower()

        # choice - search office desks
        if choice == "desks":
            print(
                "There are two desks in the office. The front desk and the nurses desk. Maybe you should check both desks. \n")

            print(
                "Which would you like to search: front desk or nurses desk?", end="")
            choice = input().lower()
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
            print(
                "It's hard to see around. You hear a some sort of thudding sound down the hall")
            self.clinic_front_office_dark()

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
                choice = input().lower()
                while choice not in ['yes', 'no']:
                    choice = input().lower()
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
        print("Would you like to search the desks or the office? Choose office or desks: ", end="")
        choice = input().lower()
        while choice not in ['office', 'desks']:
            print("Invalid input: please enter 'office' or 'desks'", end="")
            choice = input().lower()
        if choice == "desks":
            print(
                "There are two desks in the office. The front desk and the nurses desk. Maybe you should check both desks \n")

            print(
                "Which would you like to search: front desk or nurse desk? ", end="")
            choice = input().lower()
            while choice not in ['front desk', 'nurse desk']:
                print("Invalid input: please enter 'front desk' or 'nurse desk'", end="")
                choice = input().lower()
            if choice == "front desk":
                print("You searched the front desk. You find a flashlight!\n")
                self.flashlight = True
                self.clinic_front_office_light()
            if choice == "nurse desk":
                print(
                    "You search the nurses desk. You find a key to the clinic lobby door! \n")
                self.clinic_key = True
                self.clinic_front_office_light()

        elif choice == "office":
            print("The office is a mess. There is blood on the ground near the office door. Patient records and memos strewn everywhere. Some sort of fight happened here. There's also a newspaper article\n")
            self.news_or_blood()

    def news_or_blood(self):
        print("Investigate newspaper, blood, Or, go back?", end="")
        choice = input().lower()
        while choice not in ['newspaper', 'blood', 'go back']:
            print(
                "Invalid input: please enter 'newspaper','blood', or 'go back': ", end="")
            choice = input().lower()

        if choice == "newspaper":
            print("You see a newspaper titled, 'SCIENTIST MAKE BREAKTHROUGH DISCOVERY IN LOCAL LAB', circled in red with a note 'this is why i hear the whispers...... I AM NOT CRAZY!!! ITS THEM!'\n")
            self.news_or_blood()

        if choice == "blood":
            print("You find a pool of blood on the floor near the office door. It looks like someone was dragged into the door. Near the door you find a bloody screwdriver. You pick up the screwdriver.\n")
            self.screwdriver = True
            self.news_or_blood()

        elif choice == "go back":
            self.front_desk()

    def front_desk(self):
        print("You are by the front desk. Jump over to the lobby or stay here? Choose lobby or stay: ", end="")
        choice = input().lower()
        while choice not in ['lobby', 'stay']:
            print("Invalid input: please enter 'lobby' or 'stay'", end="")
            choice = input()
        if choice == "lobby":
            self.play_lobby()
        if choice == "stay":
            self.play_clinic_front_office()

    def clinic_hallway(self):
        print("As you slowly open the door you notice that it's pitch black in the hallway. \n")
        print("There are are light swtiches in your view, do you turn on the lights? yes or no? ")
        choice = input().lower()
        while choice not in ['yes', 'no']:
            print("Invalid input: please enter 'yes' or 'no': ", end="")
            choice = input().lower()
        if choice == "yes":
            print("You attempt to turn on the lights, but they don't work..... \n")
            self.clinic_hallway_down()
        if choice == "no":
            print("You turn on your flashlight. \n")
            self.clinic_hallway_down()

    def clinic_hallway_down(self):
        print("You slowly creep down the dark hallway with only a flashlight. You are searching for an examination room. \n")
        print("Every so often you see bloody footprints on the ground...\n")
        print(
            "After a few feet walking down the hallway, you see an office on your right \n")
        print("You approach the office door. You shine your flashilight on the door and it illuminates 'Dr. Raymond Bruhls")
        print("You hear a soft wheezing on the other side of the door. Labored breathing and it sounds like someone is in pain.")
        print("Do you use go in the office? Yes or no? ", end="")
        choice = input().lower()
        while choice not in ['yes', 'no']:
            print("Invalid input: please enter 'yes' or 'no'")
            choice = input().lower()
        if choice == "yes":
            self.doctors_office()
        if choice == "no":
            print("You decide not to take a chance. Something is seriously wrong here \n")
            self.exam_room()

    def doctors_office(self):
        print("You decide to enter the door. You slowly put the key in door and open it \n")
        print("You shine your light around the room and spot Dr. Bruhls laying on the floor. Covered in his own blood and barely breathing \n")
        print("You shut the door silently behind you and lock it. Barely reacts to your sudden presence as he looks at you with half dead eyes. \n")
        print(
            "You've got to get out of here... he says weakly. There's no hope for me...\n")
        print("Would you like to ask him questions? Yes or no? ", end="")
        choice = input().lower()
        while choice not in ['yes', 'no']:
            print("Invalid input: please enter 'yes' or 'no'")
            choice = input().lower()
        if choice == "yes":
            self.ask_doctor()
        if choice == "no":
            print("You're stunned by the grusome sight. You appologize and slowly back away. You hear a thud down the hall")
            print("You make your way out of the doctors office and see a door for an exam room right beside the office. Further down the hall you hear another thud")
            self.exam_room()

    def ask_doctor(self):
        print("Ask him: what happened, medical supplies, or go back? ", end="")
        choice = input().lower()
        while choice not in ['what happened', 'medical supplies', 'back']:
            print(
                "Invalid input: please enter 'what happened', 'medical supplies', or, back'")
            choice = input().lower()
        if choice == "what happened":
            print(
                "Im not sure, everyone in town went crazy. Most ran, some stayed. They all started killing each other. My nurses went crazy and one of them stabbed me... she's still around\n")
            self.ask_doctor()

        if choice == "medical supplies":
            print(
                "Right beside my office is an exam room. You can get what you need there. But be quiet \n")
            self.ask_doctor()
        if choice == "back":
            print(
                "You slowly back away and leave the doctor and make your way out the door to the exam room. \n")
            self.exam_room()

    def exam_room(self):
        print("You enter the exam room and see a red bag on the counter. Inside the bag is the medical supplies you need to help your head. \n")
        print("As you start rifling through the bag to get gauze and painkillers, you're reminded of how bad your heard hurts. You wish this was all a dream you could wake up from \n")
        print("just as you get fixed up, you hear something walk past your room. Followed by a loud crash. Something just broke in the office door. \n")
        print("You grab what you can as you hear the doctor be preyed on. \n")
        print("Do you run for it or try and help the doctor? Run or fight? ", end="")
        choice = input().lower()
        while choice not in ['run', 'shoot']:
            print("Invalid input: please enter 'run'. You have no other option. Do you think you can beat this psycho murderer?! \n")
            choice = input().lower()
        if choice == "run":
            print("You flee with all your speed and might whith the supplies. You're running down a dark hall. You hear footsteps attempting to keep up with you!")
            print("RUN RUN RUN! RUN FOR YOUR LIFE!!! \n")
            print("The door is just ahead, you decide to turn around and throw your flashlight at her while opening the door. You catch a glimpse of her scarred ragged face. There doesn't seem to be anything human left behind her eyes \n")
            print("You escape! And you made it out alive. It doesn't seem like she's chasing you anymore as you make your way out of the lobby of the clinic and back on the streets.\n")

            self.end_room_one()
        if choice == "shoot":
            print("You found the easteregg. You pull out a shotgun out of nowhwere and shoot her. You had one shot and you made it count. You safely walk out and completed your objective \n")

            self.end_room_one()

    def back_to_main(self):
        return

    # end export key to main

    def end_room_one(self):

        self.key += 1

        # print(f"You now have {self.key} keys")

    # def test_room_one(self):
    #     choice = input("Would you like to get another key? (y/n)")
    #     print(f"You now have {self.key} keys")

    #     if choice.lower() == "y":d
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
