# from main import COLOR, print_slow

# COUNTY MARKET
# Items to find to pass
# Batteries == KEY for rm2
# Snacks
# Water
# scene: front desk 'back in five', aisles, stock room (attacked by crawler, finds batteries), office/break room
# enemies: 'crawler'
# description: shadow creature that stalks prey from the shadows

from time import sleep

class rm2:
    def __init__(self, main):
        self.key = main.key
        self.batteries = False
        self.basket = False
        self.life = main.life
    def play_rm2(self):
        while self.life == True:
            self.play_market()

    def play_market(self):
        test_market = input("Would you like to play the market? (y/n) : \n")
        test_market_keys = input("Would you like to increment keys? (y/n) : \n")
        set_life_false = input("Would you like to set life to false? (y/n) : \n")
        if test_market.lower() == "y":
            self.play_room_two()
        if test_market_keys.lower() == "y":
            self.key += 1
            return {"key": self.key, "life": self.life}
        if set_life_false.lower() == "y":
            self.life = False
            print("you died")
            #return {"key": self.key, "life": self.life}
        else:
            print("Oh no! \nYour stomach rumbles and you feel dehydrated. \nYou guess that can wait for later...\n")
            print(f"Keys: {self.key}")
        return self.key

    def play_room_two(self):
        print("You walk down a dusty road to a building with the sign \n'County Market' on the front.\nYou notice the sign is worn. \nLooks like some of the letters need to be replaced...")
        sleep(3)
        print("Your stomach rumbles again loudly... \nYour mouth is starting to feel parched...\nYou decide now is a good time to pick up some snacks, \nwater and maybe batteries for your flashlight...?\n")
        sleep(3)
        print("The door jingles and creaks open... \nand take a look around...\n")
        sleep(3)
        print("The inside is dimly-lit... \nthe front counter and shelves look pretty dusty\nThere's a sign on the counter that reads: \n 'Back In Five' \n")
        sleep(3)
        self.explore_market()

    def explore_market(self):
        choose_explore_or_die = input("Would you like to SHOP around? (y/n)")
        if choose_explore_or_die.lower() == "y":
            print("You decide to look around the store... \n")
            print("You notice there's some baskets available...\n")
            pick_up_basket = input("Do you want to pick up a basket? (y/n)\n")
            if pick_up_basket.lower() == "y":
                print("You now have a BASKET. You can now... ")
                self.basket = True
                self.aisle_or_stock()
            if pick_up_basket.lower() == "n":
                self.aisle_or_stock()
        else:
            print("You wait...and wait...\n Seems like no one is coming...")
            wait_or_leave = input("Do want to keep waiting? (y/n)\n")
            if wait_or_leave.lower() == "y":
                print("You decide to keep waiting...\n")
                sleep(5)
                print("Suddenly...\n")
                sleep(1)
                print(
                    "You hear scratching noises...and a low, deep growl in the darkness behind you...\n")
                sleep(2)
                print("Oh no...it's too late...\n")
                sleep(3)
                print("A twisted, frightening, humanoid creature lunges out of the shadows at you...\nit's face distorted with \n eyes gaunt and gleaming with ravenous hunger\n")
                sleep(1)
                print("As the creature sinks its razer-sharp teeth \ninto the exposed flesh of your neck, \nand your life flashes before your eyes... \n")
                sleep(1)
                print("You think of Linda... and how \nchoosing to do nothing led to your demise...\nhow she probably figured you'd end up like this one day\n")
                sleep(1)
                print("Oh well...maybe next time you'll \nmake more interesting choices instead of waiting \naround all day for something to happen...\n")
                sleep(1)
#!!!!!!!NEED TO END GAME HERE!!!!!!!!!!!!!!
                print("GAME OVER")
            if wait_or_leave.lower() == "n":
                leave_or_continue = input("Do want to leave? (y/n)\n")
                if leave_or_continue.lower() == "y":
                    print("Suddenly...\n")
                    sleep(1)
                    print(
                        "You hear scratching noises...and a low, deep growl in the darkness behind you...\n")
                    sleep(2)
                    print("A twisted, frightening, humanoid creature lunges out of the shadows at you...\nit's face distorted with \n eyes gaunt and gleaming with ravenous hunger\n")
                    sleep(1)
                    print("As the creature sinks its razer-sharp teeth \ninto the exposed flesh of your neck, \nand your life flashes before your eyes... \n")
                    sleep(1)
                    print("You think of Linda... and how \nchoosing to run away led to your demise...\nhow she probably figured you'd end up like this one day\n")
                    sleep(1)
                    print(
                        "Oh well...maybe next time you'll \nmake more interesting choices instead of \nrunning away from all of your problems...\n")
                    sleep(1)
                    print("GAME OVER")
                    self.life == False
                    return     
                if leave_or_continue.lower() == "n":
                    print("Cool, you decided to take a look around")
                    self.aisle_or_stock()

    def aisle_or_stock(self):
        print("You start walking down the aisles when you notice an open door to what looks like a storage room...")
        # shop_or_room = input("Do you want to check out the room or keep shopping? (Choose: ROOM or SHOP)\n")

        choice = input("Would you like to make a choice? (y/n)")

        if choice.lower() == "y":
            print("RM2: Yes? Jokes on you - you never had a choice")
        else:
            print("RM2: NO!? Jokes on you - you never had a choice")


#test_rm2 = rm2("self")

