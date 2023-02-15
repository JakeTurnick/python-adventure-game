# COUNTY MARKET
# Items to find to pass
# !!!!!! Batteries == KEY for rm2 !!!!!
# LINE 255:  def go_next(self) -> returns key to main.py
# Snacks
# Water
# scene: front desk 'back in five', aisles, stock room (attacked by crawler, finds batteries), office/break room
# enemies: 'crawler'
# description: shadow creature that stalks prey from the shadows

import random
import time
from time import sleep
from colorama import init, Fore, Style
init(autoreset=True)


class rm2:
    def __init__(self, main):
        self.key = main.key
        self.batteries = False
        self.basket = False
        self.life = main.life

    COLORS = [Fore.GREEN, Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    def printslow(self, message, COLORS):
        for c in message:
            print(COLORS + c, end='', flush=True)
            time.sleep(0.001)
            print(Style.RESET_ALL, end='', flush=True)

    def play_rm2(self):
        while self.life == True:
            self.play_market()

    def play_market(self):
        #while self.life == True:    
        test_market = input("Would you like to play the market? (y/n) : \n")
        if test_market.lower() == "y":
            self.play_room_two()
            return {"key": self.key, "life": self.life} 

            # test_market_keys = input("Would you like to increment keys? (y/n) : \n")
            # if test_market_keys.lower() == "y":
            #     self.key += 1
            #     return {"key": self.key, "life": self.life}

            # set_life_false = input("Would you like to set life to false? (y/n) : \n")
            # if set_life_false.lower() == "y":
            #     print("GAME OVER")
            #     self.life = False
            #     return {"key": self.key, "life": self.life}   

            # else:
            #     print("Oh no! \nYour stomach rumbles and you feel dehydrated. \nYou guess that can wait for later...\n")
            #     #print(f"Keys: {self.key}")
            #     #return self.key
                #return 

    def play_room_two(self):
        
        self.printslow(("You walk down a dusty road to a building with the sign \n'County Market' on the front.\nYou notice the sign is worn. \nLooks like some of the letters need to be replaced..."), self.COLORS[0])
        sleep(3)
        self.printslow(("Your stomach rumbles again loudly... \nYour mouth is starting to feel parched...\nYou decide now is a good time to pick up some snacks, \nwater and maybe batteries for your flashlight...?\n"), self.COLORS[0])
        sleep(3)
        self.printslow(("The door jingles and creaks open... \nand take a look around...\n"), self.COLORS[0])
        sleep(3)
        self.printslow(("The inside is dimly-lit... \nthe front counter and shelves look pretty dusty\nThere's a sign on the counter that reads: \n 'Back In Five' \n"), self.COLORS[0])
        sleep(3)

        self.explore_market()

    def explore_market(self):
        choose_explore_or_die = input("Would you like to shop around? (y/n)")
        if choose_explore_or_die.lower() == "y":
            self.printslow(("You decide to look around the store... \n"), self.COLORS[0])
            self.printslow(("You notice there's some baskets available...\n"), self.COLORS[0])
            pick_up_basket = input("Do you want to pick up a basket? (y/n)\n")
            if pick_up_basket.lower() == "y":
                self.printslow(("You now have a BASKET. Might come in handy... \n"), self.COLORS[4])
                self.basket = True
                self.aisle_or_stock()
            if pick_up_basket.lower() == "n":
                self.aisle_or_stock()
        else:
            self.printslow(("You wait...and wait...\n Seems like no one is here..."), self.COLORS[0])
            leave_or_continue = input("Do want to leave? (y/n)\n")
            if leave_or_continue.lower() == "y":
                self.printslow(("Suddenly...\n"), self.COLORS[0])
                sleep(1)
                self.printslow((
                    "You hear scratching noises...and a low, deep growl in the darkness behind you...\n"), self.COLORS[1])
                sleep(2)
                self.printslow(("A twisted, frightening, humanoid creature lunges out of the shadows at you...\nit's face distorted with \n eyes gaunt and gleaming with ravenous hunger\n"), self.COLORS[1])
                sleep(1)
                self.printslow(("As the creature sinks its razer-sharp teeth \ninto the exposed flesh of your neck, \nand your life flashes before your eyes... \n"), self.COLORS[1])
                sleep(1)
                self.printslow(("You think of Linda... and how \nchoosing to run away led to your demise...\nhow she probably figured you'd end up like this one day\n"), self.COLORS[1])
                sleep(1)
                self.printslow((
                    "Oh well...maybe next time you'll \nmake more interesting choices instead of \nrunning away from all of your problems...\n"), self.COLORS[1])
                sleep(1)
                self.printslow(("GAME OVER"), self.COLORS[1])
                self.life = False
                return {"key": self.key, "life": self.life} 
            if leave_or_continue.lower() == "n":
                self.printslow(("Cool, you decided to take a look around...\nThe shelves look pretty dark and empty.\n You touch one and notice a layer of dust left on your finger...\n"), self.COLORS[0])
                self.aisle_or_stock()

    def aisle_or_stock(self):
        self.printslow(("You start walking down the aisles when you notice an open door \nto what looks like a storage room...\n"), self.COLORS[0])

        while True:
            shop_or_room = input("Do you want to investigate the room? (y/n)")
            if shop_or_room.lower() == "y":
                self.printslow(("You chose to investigate the room ... \n"), self.COLORS[0])
                self.investigate_room()
                break
            elif shop_or_room.lower() == "n":
                self.printslow(("You chose to keep shopping ...\n"), self.COLORS[0])
                self.keep_shopping()
                break
            else:
                self.printslow(("Please choose either 'y' or 'n'\n"), self.COLORS[4])

    def investigate_room(self):
        self.printslow(("The room is dark and very poorly lit... \nyou hear scratching behind you, \nbut can't figure out what's making the sound...no one is here. \n"), self.COLORS[0])

        while True:
            leave_room = input("Turn around? (y/n?)")
            if leave_room.lower() == "n":
                self.printslow(("You chose to keep looking around the room... \n You see an old journal on the table"), self.COLORS[0])
                break
            elif leave_room.lower() == "y":
                self.printslow(("You chose to leave the room ...\n"), self.COLORS[0])
                sleep(2)
                self.printslow(("You turn around and ...\n"), self.COLORS[0])
                sleep(2)
                self.printslow(("You see a massive humanoid creature with razor-sharp teeth, \ndark-beady eyes and wide, gapping mouth...\n"), self.COLORS[1])
                sleep(2)
                self.printslow(("It lets out an omnious growl...\n"), self.COLORS[1])
                sleep(2)
                self.printslow(("And lunges for your throat...\n"), self.COLORS[1])
                if self.basket == True:
                    self.printslow(("You blocked the creature's attack with the basket!!\n You throw it at the creature and it shrinks back into the shadows...\n You decide it's best to run back to the front of the store...\n"), self.COLORS[0])
                    sleep(2)
                    self.locate_key()
                    break
                    # print("You breathe a sigh of relief...that was close...") 
                else:
                    damage = random.randint(0, 30)
                    if damage < 20:
                        self.printslow(("That was quick thinking! \n You blocked the creature's attack with a broom!\n The creature shrinks back into the shadows! \n Better get out quick! \n"), self.COLORS[0])
                        self.locate_key()
                        break
                    else:
                        self.printslow(("The creature stares at you with it's beady eyes... \nit cuts off your escape and sinks it's teeth into you!\n In your last moments, you think about Linda... \nHow much you'll miss her...\n"), self.COLORS[1])
                        self.printslow(("Game over, nice try!\n"), self.COLORS[1])
                        self.life = False
                        return {"key": self.key, "life": self.life} 
            else:
                self.printslow(("Please choose either 'y' or 'n'"), self.COLORS[4])

    def keep_shopping(self):
        self.printslow(("As you walk down one of the snack aisles, \nyou notice a note next next to some snacks...\n"), self.COLORS[3])
        sleep(2)
        self.printslow(("By aisle and shelf, I do reside,\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("In shadows deep, I do bide.\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("A spark of life, a power bright,\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("To help thee on thy way to night.\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("The quiet whispers, they do tell,\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("Where I do lie, in shadows dwell.\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("Seek thou, but wisely, in thy quest,\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("For I am found, when all is at rest.\n"), self.COLORS[0])
        sleep(1)
        self.printslow(("...what a weird note...\n"), self.COLORS[0])
        sleep(3)
        while True:
            inspect_shelves = input("Do you want to inspect the shelves? (y/n)")
            sleep(3)
            if inspect_shelves.lower() == "y":
                self.printslow(("You chose to inspect the shelves ...\n You grab it and wiggle... \n Out pops... "), self.COLORS[0])
                sleep(2)
                self.printslow(("...batteries...for your flashlight to change your tire!"), self.COLORS[0])
                sleep(2)
                self.batteries = True
                self.go_next()
                break
            elif inspect_shelves.lower() == "n":
                self.printslow(("Some weirdo must have left the note. \n"), self.COLORS[0])
                sleep(2)
                self.printslow(("Oh well... \n"), self.COLORS[0])
                sleep(3)
                self.printslow(("2 hours later...\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("You're trying to change your tire in the dark...\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("Would be nice to have some batteries right about now...\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("You hear leaves rustling behind you...\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("All of a sudden...a growl...from a BEAR!\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("You try to run...but you're not fast enough!\n"), self.COLORS[0])
                sleep(1)
                self.printslow(("GAME OVER, should have taken the hint\n...this was an easy one! ;)"), self.COLORS[0])
                sleep(1)
                self.life = False
                return {"key": self.key, "life": self.life} 
            else:
                self.printslow(("Please choose either 'y' or 'n'"), self.COLORS[4])
                sleep(2)

    def locate_key(self):
        sleep(3)
        self.printslow(("You quickly grab whatever you can off the shelves and make a run for it!"), self.COLORS[0])
        sleep(1)
        get_lucky = random.randint(0, 30)
        if get_lucky > 10: 
            self.printslow(("You see a note...something about... \nspark of life, a power bright,\nYou chose to inspect the shelves ...\n You grab it and wiggle... \n Out pops...\n"), self.COLORS[0])
            sleep(2)
            self.printslow(("...batteries...for your flashlight to change your tire!\n") , self.COLORS[3])
            sleep(3)
            self.batteries = True 
            var = self.go_next()
            print(var)
        else:
            self.printslow(("You get out of the store ok...but..."), self.COLORS[0])
            sleep(3)
            self.printslow(("2 hours later...\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("You're trying to change your tire in the dark...\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("Would be nice to have some batteries right about now...\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("You hear leaves rustling behind you...\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("All of a sudden...a growl...from a BEAR!\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("You try to run...but you're not fast enough!\n"), self.COLORS[0])
            sleep(1)
            self.printslow(("GAME OVER, not lucky enough I guess... :(\n"), self.COLORS[0])
            sleep(1)
            self.life = False
            return {"key": self.key, "life": self.life} 

#export keys
    def go_next(self):
        if self.batteries == True:
            self.printslow(("Well...that was weird...but...\n"), self.COLORS[0])
            sleep(3)
            self.printslow(("You leave the store...\nYou passed the room sucessfully!"), self.COLORS[0])
            sleep(3)
            self.key += 1
          
        else:
            self.printslow(("Oops, something weird happened.\n"), self.COLORS[1])
            sleep(1)
            self.printslow(("Try again.\n"), self.COLORS[1])
            sleep(1)