class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f"{self.restaurant_name.title()} makes {self.cuisine_type}")


def main():
    little_shop = Restaurant('the little shop', 'burgers')
    taco_stand = Restaurant("Holy Guacamole", "tacos")

    little_shop.describe_restaurant()
    taco_stand.describe_restaurant()

if __name__ == "__main__":
    main()