# Concession stand program:

menu = {"Ice-cream": 3.00,
        "pizza": 12.00,
        "popcorn": 8.00,
        "chips": 2.00,
        "drink": 7.50,
        "soda": 5.00,
        "potato": 1.70,
        "water": 0.50,
        "all-items": 36.70}
cart = []
total = 0

print("---------MENU-----------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item: ").lower()
    if food == "c":
        break
    elif food == "":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------------YOUR LIST------------")
for food in cart:
    total += menu.get(food)
print()
print(f"Total is: ${total:.2f}")
if total > 0:
    print("buy now?(y/n)" )
    wanted_to_buy = input()
    def purchase() :
        if wanted_to_buy == "y":
            global money
            money = 0
            print(f"Give {total:.2f}$ for buy: ")
            try:
                money = float(input())
            except ValueError:
                print("that wasn't a float or integer number.")
            if money > total:
                remain = money - total
                print(f"Wait! You'll get {remain:.2f}$ back.")
            elif money < total:
                print(f"There's no discount, sir. You need pay {total:.2f}$")
                purchase()
            elif money == total:
                print("Thanks.")
            else:
                print("WTF")
        else:
            print("no problem.")
    purchase()
else:
    print("You didn't select any items!")
