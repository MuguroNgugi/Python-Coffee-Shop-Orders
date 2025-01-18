#Python Coffee Shop Orders
#A sample script to calculate the total cost of a cup of coffee based on the user preferences

print("Welcome to Python Coffe Shop Orders")

#Function to get valid inputs for coffee size
def get_coffee_size():
    while True:
        size = input("What coffee size do you want? S, M, L: ").lower()
        if size in ["s", "m", "l"]:
            return size
        else:
            print("You entered the wrong inputs. Kindly try again")

#Function to get valid inputs for optional toppings
def get_optional_toppings_one():
    while True:
        optional_toppings_one = input("Do you want whipped cream? Y or N: ").lower()
        if optional_toppings_one in ["y", "n"]:
            return optional_toppings_one
        else:
            print("You entered wrong inputs. Kindly try again")

def get_optional_topping_two ():
    while True:
        optional_toppings_two = input("Do you want caramel syrup? Y or N: ")
        if optional_toppings_two in ["y", "n"]:
            return optional_toppings_two
        else:
            print("You entered wrong inputs. Kindly try again")

#Function to get inputs for a reusable cup for a discount
def get_reusable_cup_discount ():
    while True:
        reusable_cup = input("Will you bring a reusable cup? Y or N: ")
        if reusable_cup in ["y", "n"]:
            return reusable_cup
        else:
            print("You entered wrong inputs. Kindly try again")

#get user inputs with validations
size = get_coffee_size()
optional_toppings_one = get_optional_toppings_one()
optional_toppings_two = get_optional_topping_two()
reusable_cup = get_reusable_cup_discount()

#Calculate cost of a cup of coffee
bill = 0
if size == "s":
    bill += 5
elif size == "m":
    bill += 10
elif size == "l":
    bill += 15

#Calculate cost of optional toppings
if optional_toppings_one == "y":
    bill += 2
if optional_toppings_two == "y":
    bill += 3

#Calculate reusable cup discount
if reusable_cup == "y":
    bill -= 1

#Output total bill
print(f"\nYour total bill is ${bill}")
if reusable_cup == "y":
    print("Thank you for supporting us 👍!")