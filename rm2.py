# from main import COLOR, print_slow

# COUNTY MARKET
# Items to find to pass
# Batteries == KEY for rm2
# Snacks
# Water
# scene: front desk 'back in five', aisles, stock room (attacked by crawler, finds batteries), office/break room
# enemies: 'crawler'
# description: shadow creature that stalks prey from the shadows
import random
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
        while self.life == True:
                    
            test_market = input("Would you like to play the market? (y/n) : \n")
            if test_market.lower() == "y":
                self.play_room_two()

            test_market_keys = input("Would you like to increment keys? (y/n) : \n")
            if test_market_keys.lower() == "y":
                self.key += 1
                #return {"key": self.key, "life": self.life}

            set_life_false = input("Would you like to set life to false? (y/n) : \n")
            if set_life_false.lower() == "y":
                print("GAME OVER")
                self.life = False
                return {"key": self.key, "life": self.life}   

            else:
                print("Oh no! \nYour stomach rumbles and you feel dehydrated. \nYou guess that can wait for later...\n")
                print(f"Keys: {self.key}")
                #return self.key


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
        choose_explore_or_die = input("Would you like to shop around? (y/n)")
        if choose_explore_or_die.lower() == "y":
            print("You decide to look around the store... \n")
            print("You notice there's some baskets available...\n")
            pick_up_basket = input("Do you want to pick up a basket? (y/n)\n")
            if pick_up_basket.lower() == "y":
                print("You now have a BASKET. Might come in handy... ")
                self.basket = True
                self.aisle_or_stock()
            if pick_up_basket.lower() == "n":
                self.aisle_or_stock()
        else:
            print("You wait...and wait...\n Seems like no one is here...")
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
                self.life = False
                return {"key": self.key, "life": self.life} 
            if leave_or_continue.lower() == "n":
                print("Cool, you decided to take a look around...\nThe shelves look pretty dark and empty.\n You touch one and notice a layer of dust left on your finger...\n")
                self.aisle_or_stock()

    def aisle_or_stock(self):
        print("You start walking down the aisles when you notice an open door to what looks like a storage room...")

        while True:
            shop_or_room = input("Do you want to investigate the room? (y/n)")
            if shop_or_room.lower() == "y":
                print("You chose to investigate the room ... ")
                self.investigate_room()
                break
            elif shop_or_room.lower() == "n":
                print("You chose to keep shopping ...")
                self.keep_shopping()
                break
            else:
                print("Please choose either 'y' or 'n'")

    def investigate_room(self):
        print("You decided to investigate the stock room...\nthe room is dark and very poorly lit... \nyou hear scratching behind you, \nbut can't figure out what's making the sound...no one is here. \n")

        while True:
            leave_room = input("Turn around? (y/n?)")
            if leave_room.lower() == "n":
                print("You chose to keep looking around the room... \n You see an old journal on the table")
                break
            elif leave_room.lower() == "y":
                print("You chose to leave the room ...\n")
                sleep(2)
                print("You turn around and ...\n")
                sleep(2)
                print("You see a massive humanoid creature with razor-sharp teeth, \ndark-beady eyes and wide, gapping mouth...\n")
                sleep(2)
                print("It lets out an omnious growl...\n")
                sleep(2)
                print("And lunges for your throat...\n")
                if self.basket == True:
                    print("You blocked the creature's attack with the basket!!\n You throw it at the creature and it shrinks back into the shadows...\n You decide it's best to run back to the front of the store...\n")
                    sleep(2)
                    self.locate_key()
                    break
                    # print("You breathe a sigh of relief...that was close...") 
                else:
                    damage = random.randint(0, 30)
                    if damage < 20:
                        print("That was quick thinking! \n You blocked the creature's attack with a broom!\n The creature shrinks back into the shadows! \n Better get out quick! \n")
                        self.locate_key()
                        break
                    else:
                        print("The creature stares at you with it's beady eyes... \nit cuts off your escape and sinks it's teeth into you!\n In your last moments, you think about Linda... \nHow much you'll miss her...\n")
                        print("Game over, nice try!\n")
                        self.life = False
                        return {"key": self.key, "life": self.life} 
            else:
                print("Please choose either 'y' or 'n'")

    def keep_shopping(self):
        print("You chose to keep shopping...\nAs you walk down one of the snack aisles, \nyou notice a note next next to some snacks...\n")
        print("By aisle and shelf, I do reside,\n")
        print("In shadows deep, I do bide.\n")
        print("A spark of life, a power bright,\n")
        print("To help thee on thy way to night.\n")
        print("The quiet whispers, they do tell,\n")
        print("Where I do lie, in shadows dwell.\n")
        print("Seek thou, but wisely, in thy quest,\n")
        print("For I am found, when all is at rest.\n")
        print("...what a weird note...\n")

        while True:
            inspect_shelves = input("Do you want to inspect the shelves? (y/n)")
            if inspect_shelves.lower() == "y":
                print("You chose to inspect the shelves ...\n You grab it and wiggle... \n Out pops... ")
                print("...batteries...for your flashlight to change your tire!")
                self.batteries = True
                self.go_next()
                break
            elif inspect_shelves.lower() == "n":
                print("Some weirdo must have left the note. \n")
                print("Oh well... \n")
                print("2 hours later...\n")
                print("You're trying to change your tire in the dark...\n")
                print("Would be nice to have some batteries right about now...\n")
                print("You hear leaves rustling behind you...\n")
                print("All of a sudden...a growl...from a BEAR!\n")
                print("You try to run...but you're not fast enough!\n")
                print("GAME OVER, should have taken the hint\n...this was an easy one! ;)")
                self.life = False
                return {"key": self.key, "life": self.life} 
            else:
                print("Please choose either 'y' or 'n'")

    def locate_key(self):
        print("You quickly grab whatever you can off the shelves and make a run for it!")
        get_lucky = random.randint(0, 30)
        if get_lucky > 10: 
            print("You see a note...something about... \nspark of life, a power bright,\nYou chose to inspect the shelves ...\n You grab it and wiggle... \n Out pops... ")
            print("...batteries...for your flashlight to change your tire!") 
            self.batteries = True 
            self.go_next()
        else:
            print("You get out of the store ok...but...")
            print("2 hours later...\n")
            print("You're trying to change your tire in the dark...\n")
            print("Would be nice to have some batteries right about now...\n")
            print("You hear leaves rustling behind you...\n")
            print("All of a sudden...a growl...from a BEAR!\n")
            print("You try to run...but you're not fast enough!\n")
            print("GAME OVER, not lucky enough I guess... :(")
            self.life = False
            return {"key": self.key, "life": self.life} 

    def go_next(self):
        if self.batteries == True:
            print("Well...that was weird...but...\n")
            print("You leave the store...You passed the room sucessfully!")
            self.key += 1
            return {"key": self.key, "life": self.life} 
        else:
            print("Oops, something weird happened.\n")
            print("Try again.\n")