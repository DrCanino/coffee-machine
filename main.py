
# amount of ingredients needed per cup
WATER_PER_CUP = 200  # ml
MILK_PER_CUP = 50    # ml
BEANS_PER_CUP = 15   # g

# ask the user for available resources
water = int(input("Write how many ml of water the coffee machine has:\n> "))
milk = int(input("Write how many ml of milk the coffee machine has:\n> "))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n> "))

# ask for number of cups desired
cups_needed = int(input("Write how many cups of coffee you will need:\n> "))

# calculate how many cups can be made with available resources
cups_possible = min(water // WATER_PER_CUP,
                    milk // MILK_PER_CUP,
                    beans // BEANS_PER_CUP)

# decision
if cups_possible == cups_needed:
    print("Yes, I can make that amount of coffee")
elif cups_possible > cups_needed:
    extra = cups_possible - cups_needed
    print(f"Yes, I can make that amount of coffee (and even {extra} more than that)")
else:
    print(f"No, I can make only {cups_possible} cup(s) of coffee")
