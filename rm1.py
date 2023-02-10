class rm1_class:
    def __init__(self, key):
        self.key = key
        # key passed in from Main_Game creating new rm1_class

    def play_room_one(self):
        choice = input("Would you like to make a choice? (y/n)")

        if choice.lower() == "y":
            print(self.key)
            self.key += 1
            print(self.key)
            print("RM1: Yes? Jokes on you - you never had a choice")
        else:
            print("RM1: NO!? Jokes on you - you never had a choice")
