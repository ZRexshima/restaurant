from time import sleep
from random import randint

from restaurant import Restaurant


def main():
    little_shop = Restaurant("the little shop", "burgers")
    taco_stand = Restaurant("Holy Guacamole", "tacos")
    fifi_soba = Restaurant("fifi's soba", "soba")

    little_shop.describe_restaurant()
    taco_stand.describe_restaurant()
    fifi_soba.describe_restaurant()
    sleep(2)

    little_shop.set_number_served(100)
    little_shop.print_number_served()

    while little_shop.number_served < 200:
        serving = randint(0, 10)
        difference = 200 - little_shop.number_served
        if difference < serving:
            little_shop.increment_number_served(difference)
            little_shop.print_number_served()
            break
        else:
            little_shop.increment_number_served(serving)
            little_shop.print_number_served()
            sleep(1)


if __name__ == "__main__":
    main()
