class rm1_class:
    def __init__(self, key):
        self.key = key
        # key passed in from Main_Game creating new rm1_class

    def play_room_one(self):
        choice = input("")
        print("You enter the lobby of the clinic. You are looking for gauze to wrap your head wound and some pain killers")
        print("The lobby looks like a mess. Some chairs have been thrown about and a waste toppled over. There is a desk to the office in front of you, and a door into the clinic on your right. ")
        print("Check door or desk?: ", end="")
        choice

        print("You found a key, would you like to pick it up?")

        if choice.lower() == "door":

            print("You go to the door, It's locked. You need to find a key or maybe pick the lock? ")
            if self.key == "clinic key" or self.key == "screwdriver":
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
        



        # print(self.key)
        
        if choice.lower() == "desk":
            self.key += 1
            print(self.key)
            print("RM1: Yes? Jokes on you - you never had a choice")
        else:
            print("RM1: NO!? Jokes on you - you never had a choice")
