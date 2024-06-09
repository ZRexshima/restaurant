from restaurant import IceCreamStand


def test_frosty():
    frosty = IceCreamStand("Frosty Kool")
    frosty.describe_restaurant()
    frosty.set_number_served(50)
    frosty.print_number_served()
    frosty.increment_number_served(5)
    frosty.print_number_served()
    print()
    delivery = ["chocolate", "mint", "peanut-butter", "mystery"]
    frosty.add_flavors(*delivery)
    frosty.display_flavors()


if __name__ == "__main__":
    test_frosty()
