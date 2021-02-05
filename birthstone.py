# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

# no input validation requirement in instructions - DDG
print("\n\n\n\nBirthstone\n\n")

user_input = input("Enter the number of the month you were born (1-12)")
month = int(user_input)


if month == 1:
    print("Your birthstone is garnet\n\n")

elif month == 2:
    print("Your birthstone is amethyst\n\n")

elif month == 3:
    print("Your birthstone is aquamarine\n\n")

elif month == 4:
    print("Your birthstone is diamond\n\n")

elif month == 5:
    print("Your birthstone is emerald\n\n")

elif month == 6:
    print("Your birthstone is pearl or alexandrite\n\n")

elif month == 7:
    print("Your birthstone is ruby\n\n")

elif month == 8:
    print("Your birthstone is peridot\n\n")

elif month == 9:
    print("Your birthstone is sapphire\n\n")

elif month == 10:
    print("Your birthstone is tourmaline or opal\n\n")

elif month == 11:
    print("Your birthstone is topaz or citrine\n\n")

elif month == 12:
    print("Your birthstone is tanzanite, zircon or turquoise\n\n")
