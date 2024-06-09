from string import capwords


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
    flavors: list[str] = []

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)

    def display_flavors(self):
        if self.flavors:
            print(f"{self.restaurant_name} has the following flavors:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
