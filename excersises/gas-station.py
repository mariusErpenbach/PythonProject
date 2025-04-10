oilPrices = {"super": 1.59,
             "diesel": 1.62,
             "e10": 1.65,
             "synthetic": 1.8}


def refueling():
    print("On your way home, you realize that you are running out of gas, only 10% left.")
    oil = input("You are driving into a gas station, which type of oil do you need, friend?\n").lower()

    # Check if the oil type exists in the available stock
    if oil not in oilPrices:
        return f"Unfortunately, this gas station does not have {oil} in stock, sorry friend.\n"

    # Validate and parse budget input
    try:
        budget = float(input("You put the tank hose in your car, what is your budget, friend? \n"))
    except ValueError:
        return "Invalid budget input. Please enter a numeric value."

    # Validate and parse tankMax input
    try:
        tankMax = int(input(
            "Since you are driving a company car, you can't afford to waste any oil by overflowing the tank, what was the tank volume again? \n"))
    except ValueError:
        return "Invalid tank volume input. Please enter a valid integer."

    if tankMax < 5:
        return "Please fuel your bobbycar by hand."

    # Calculate the maximum amount of fuel you can buy based on your budget
    price_per_liter = oilPrices[oil]
    max_liters = budget / price_per_liter  # how much oil can the user afford with his budget


    if max_liters > tankMax: # make sure we don`t go over the max liters
        max_liters = tankMax

    total_cost = max_liters * price_per_liter

    return f"With your budget of {budget}€, you can buy up to {max_liters:.2f} liters of {oil}. That`s {total_cost:.2f}€ please, friend."


print(refueling())