class rm1_class:
    def __init__(self, key):

        self.key = key
        self.office_key = False 
        self.supply_key = False
        self.work_id = True
        self.screwdriver = False
        self.pain_killers = False
        self.gauze = False

        self.wellness = "injured"

        # key passed in from Main_Game creating new rm1_class
  
        def play_room_one(self):
            print("Would you like to enter the clinic?")
            print("Choose yes or no: ", end="")
            choice = input("")
            print("You enter the lobby of the clinic. You are looking for gauze to wrap your head wound and some pain killers")

        def play_lobby(self):
            print("The lights are off. The lobby looks like a mess. Some chairs have been thrown about and a waste toppled over. There is a desk to the office in front of you, and a door into the clinic on your right. ")
            print("Check door or desk?: ", end="")
            choice = ("")
            if choice.lower() == "door":

                print("You go to the door, It's locked. You need to find a key or maybe pick the lock? ")
                if self.key == "clinic key" or self.screwdriver == True:
                    print("You opened the clinic door")
                    pass
                    #continue
                else: 
                    print("You can't open the door right now.")
                    print("You turn around and look at the lobby. What next?")
                    print("Go to the front office desk, or go back to the lobby?", end="")
                    choice 

            if choice.lower() =="desk":
                print("You go stand in front of the desk. You could climb over and search the office.")
                print("Do you climb over?: ", end="")
                choice

                if choice.lower() =="yes":
                    print("You climb over the desk.")

                if choice.lower() =="no":
                    print("You turn around and look at the lobby")



    def play_clinic_font_office(self):
        print("You climb ontop of the desk. The office is dimly lit and what little light you see is coming from the mostly closed blinds on the walls. The office looks messy and there are signs of a struggle.")
        print("look around or open blinds?", end="")
        choice = ("")

        # def lookaround_office_front_desk(self):
        #     print("")

        #open blinds
        if choice == "open blinds" or choice == "blinds":
            print("You open the blinds and light illuminates the room. The empty streets in front of you give you chills. Dark shadows recede and you can see the office more clearly. Chairs have been knocked over, a vase had been knocked over and shattered on the floor. Various papers are scattered around the floor.")
            print("The room layout consists of the front office desk for check in and check out. Two other desks in the center of the room for other nurses. Directly in front of you are filing cabinets ")

            def clinic_floor_lights_on(self):
                pass

            def clinic_floor_lights_off(self):
                pass
        #look around in dark 


                

            



            # print(self.key)
            
            if choice.lower() == "desk":
                self.key += 1
                print(self.key)
                print("RM1: Yes? Jokes on you - you never had a choice")
            else:
                print("RM1: NO!? Jokes on you - you never had a choice")
