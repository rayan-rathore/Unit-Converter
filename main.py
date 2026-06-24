from data import UNIT_DATA
from conversionengine import ConversionEngine

data = UNIT_DATA
cat = ConversionEngine()
cat.setup_categories()

print("\n----Welcome to Unit converter!----\n")
while True:
    available_cat = cat.get_categories_name()
    print(f"Available categories : {available_cat}")
    while True:
        user_input = input("\nWhat do you want to convert? please select from above list.\n").casefold()
        if cat.is_valid_category(user_input):
            break
        else:
            print("Invalid category, Please select from Available categories!")

    available_units = cat.get_categories_units(user_input)
    print(f"\nAvailable Units : {available_units}")
    while True:
        from_u = input("\nPlease select unit from which you want to convert. "
                       "Please select from above list.\n").casefold()
        if cat.is_valid_units(user_input,from_u):
            break
        else:
            print("Invalid Unit, Please select from Available Units!")

    while True:
        try:
            value = float(input("\nWhat is the value of your chosen unit?\n"))
            break
        except ValueError:
            print("Invalid input. Please enter the number.")

    while True:
        to_u = input("\nTo which unit you want to convert that value? "
                     "Please select from above Available Units list.\n").casefold()
        if cat.is_valid_units(user_input,to_u):
            break
        else:
            print("Invalid Unit, Please select from Available Units!")

    cal = cat.execute_conversion(user_input, from_u, to_u, value)
    print(f"\n{value} {from_u.title()} is equal to {cal:.3f} {to_u.title()}.")

    user_choice = input("Would you like another conversion? (y/n)").casefold()
    if user_choice != "y":
        print("\nThanks for using Unit converter. Shutting down....")
        break

