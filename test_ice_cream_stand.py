from random import randint
from time import sleep

from restaurant import IceCreamStand


def test_frosty():
    frosty = IceCreamStand("Frosty Kool")
    frosty.describe_restaurant()
    frosty.set_number_served(50)
    frosty.print_number_served()
    sleep(2)

    goal = 100
    while frosty.number_served < goal:
        serving = randint(1, 5)
        difference = goal - frosty.number_served
        if difference < serving:
            frosty.increment_number_served(difference)
            frosty.print_number_served()
            break
        else:
            frosty.increment_number_served(serving)
            frosty.print_number_served()
            sleep(1)

    print()
    delivery = ["chocolate", "mint", "peanut-butter", "mystery"]
    frosty.add_flavors(*delivery)
    frosty.display_flavors()
    sleep(2)


if __name__ == "__main__":
    test_frosty()
