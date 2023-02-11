# Jake's room - Mechanics garage
# Goal: Obtain fresh Tire
# - Tire: Obtain Socket Wrench
# -- Socket wrench: Locked inside car with zombie
# --- Car key: Riddle from accounting
# --- Crowbar: Found in storage
# -- No crowbar? 50% chance of death
# -- Crowbar? Hold zombie back and grab socket wrench

from time import sleep


class Garage:
    def __init__(self, key):
        self.key = key
        self.flash_light = False
        self.car_key = False
        self.crowbar = False
        self.socket_wrench = False
        self.tire = False

    def play_garage(self):
        test_input = input("Would you like to play the garage? (y/n) : ")
        if test_input.lower() == "y":
            self.play_room_three()
            # self.entrance()
            # self.garage()
            # print(f"Keys: {self.key}")
        else:
            print("booo")
            print(f"Keys: {self.key}")
        # entrance
        return self.key

    def entrance(self):
        print("You enter the garage, the lights appear to be out but the store front windows allow you to see")
        sleep(.5)
        print("You walk up to the counter and peak around . . . No one seems to be aronud")
        sleep(.5)

        print("As you scan the room you spot a door labeled \"Garage\" and what could be supplies littered behind the counter")
        scan_entrance = input(
            "What do you check? (\"counter\" or \"garage\") : ")
        print(f"Scan entrance: {scan_entrance}")
        scan_test = scan_entrance.lower() == "counter" or scan_entrance.lower() == "garage"
        print(f"Scan test: {scan_test}")

        while scan_test is not True:
            scan_entrance = input(
                "Invalid input - What do you check? (\"counter\" or \"garage\") : ")
            scan_test = scan_entrance.lower() == "counter" or scan_entrance.lower() == "garage"

        if scan_entrance.lower() == "counter":

            print(
                "You see a flashlight and batteries behind the counter... almost like someone dropped them")
            take_light = input("Take the flashlight? (y/n) : ")

            # one-liner below
            # light_test = take_light.lower() == "y" or take_light.lower() == "n"
            # print(light_test)
            # while light_test is not True:
            #     take_light = input(
            #         "Invalid input - Take the flashlight? (y/n) : ")
            #     light_test = take_light.lower() == "y" or take_light.lower() == "n"

            while take_light.lower() != "y" and take_light.lower() != "n":
                take_light = input(
                    "Invalid input - Take the flashlight? (y/n) : ")

            if take_light.lower() == "y":
                print("You step behind the counter and pick up the flashlight")
                self.flash_light = True
                print("You turn the light on to verify that it works . . . it does!")
                sleep(.5)
                print(
                    "But you spot the flash lights reflection on a pool of some viscous liquid")
                sleep(.5)
                print("... it's probablt oil . . . hopefully")
                sleep(.8)
                print("With a flashlight equipped you feel ready to enter the garage")
                sleep(1)

            else:  # take_light == n
                print("A bold and brash adventurer like you don't need no damn lights")
        else:  # scan_entrance == garage
            if self.flash_light == True:
                print("You use flashlight to help you see in the large garage")
            else:
                print("With no fear, you plunge yourself into the dark garage")

    def garage(self):
        if self.flash_light == True:
            print("You open the door to the garage")
            sleep(.5)
            print("thankfully you have a flashlight")
        else:
            print("The garage is dark without a flashlight")
        pass
    # test to make sure class works

    def play_room_three(self):
        choice = input("Would you like to get another key? (y/n)")

        if choice.lower() == "y":
            print(f"RM3: You had {self.key} keys before")
            self.key += 1
            print(f"You now have {self.key} keys")
            return self.key
        else:
            print(f"RM3: You have {self.key} keys")
            return self.key


# test = Garage(key=1)
# test.play_garage()
