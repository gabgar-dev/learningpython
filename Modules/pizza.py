def make_pizza(size,*toppings):
    """Summarize the Pizza we are about to make"""
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)