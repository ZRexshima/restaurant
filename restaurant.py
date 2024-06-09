import random
from string import capwords
import time


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = capwords(restaurant_name)
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self) -> None:
        print(f"{self.restaurant_name} makes {self.cuisine_type}")

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.number_served += n

    def print_number_served(self):
        print(f"{self.restaurant_name} has served {self.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)


def main():
    little_shop = Restaurant('the little shop', 'burgers')
    taco_stand = Restaurant("Holy Guacamole", "tacos")
    fifi_soba = Restaurant("fifi's soba", "soba")

    little_shop.describe_restaurant()
    taco_stand.describe_restaurant()
    fifi_soba.describe_restaurant()

    little_shop.set_number_served(100)
    print(f"{little_shop.restaurant_name} has served {little_shop.number_served}")

    while little_shop.number_served < 200:
        serving = random.randint(0,10)
        difference = 200 - little_shop.number_served
        if difference < serving:
            little_shop.increment_number_served(difference)
            little_shop.print_number_served()
            break
        else:
            little_shop.increment_number_served(serving)
            little_shop.print_number_served()
            time.sleep(1)

    print()
    frosty = IceCreamStand("Frosty Kool")
    frosty.describe_restaurant()
    frosty.set_number_served(50)
    frosty.print_number_served()
    frosty.increment_number_served(5)
    frosty.print_number_served()


if __name__ == "__main__":
    main()
