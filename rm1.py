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
        self.screwdriver = False

        # key passed in from Main_Game creating new rm1_class
  # this initializes the game

    def play_room_one(self):
        print("Would you like to enter the clinic?")
        print("Choose yes or no: ", end="")
        choice = input()
        if choice == "yes":
            print("You enter the lobby of the clinic. You are looking for gauze to wrap your head wound and some pain killers")
            self.play_lobby()

        else:
            #if no, send player to main.py file play_main function
            pass
           

    # You enter the lobby

    def play_lobby(self):
        print("The lights are off. The lobby looks like a mess. Some chairs have been thrown about and a waste toppled over. There is a desk to the office in front of you, and a door into the clinic on your right.")
        print("Check door or desk?: ", end="")
        choice = input()
        if choice.lower() == "door":
            print(
                "You go to the door, It's locked. You need to find a key or maybe pick the lock?")
            print("Do you want to try to open the door?", end="")
            choice = input()
            if self.key == "clinic key" or self.screwdriver == True:
                print("You opened the clinic door")
                self.clinic_hallway()

            else:
                print("You don't have a key or a way to pick the lock yet.")
                self.play_lobby()

        if choice.lower() == "desk":
            print(
                "You go stand in front of the desk. You could climb over and search the office.")
            print("Do you climb over?: ", end="")
            choice = input()

            if choice.lower() == "yes":
                print("You climb over the desk.")

            else:
                choice.lower() == "no"
                print("You turn around and look at the lobby")

    # def play_clinic_font_office(self):
    #     print("You climb ontop of the desk. The office is dimly lit and what little light you see is coming from the mostly closed blinds on the walls. The office looks messy and there are signs of a struggle.")
    #     print("look around or open blinds?", end="")
    # choice = ("")

    # # def lookaround_office_front_desk(self):
    # #     print("")

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

    def test_room_one(self):
        choice = input("Would you like to get another key? (y/n)")
        print(f"You now have {self.key} keys")
        
        if choice.lower() == "y":
            # print(f"RM3: You had {self.key} keys before")
            self.key += 1
            return {"key": self.key, "life": self.life}
         
        else:
            print("You died")
            self.life = False
            return {"key": self.key, "life": self.life}

            pass

            # if choice.lower() == "desk":
            #     self.key += 1
            #     print(self.key)
            #     print("RM1: Yes? Jokes on you - you never had a choice")
            # else:
            #     print("RM1: NO!? Jokes on you - you never had a choice")
<<<<<<< HEAD
#test_rm1 = rm1_class("clinic")
#test_rm1.play_room_one()
=======

# remove the bottom test variables once you're done
# test_rm1 = rm1_class()
# test_rm1.play_room_one()
>>>>>>> e66722c (implemented a test funciton for keys and player health)
