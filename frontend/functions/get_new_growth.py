def get_new_growth():
    """
    Function to get the growth rate of a city from the user and validate it
    """

    while True:
        try:
            growth = float(
                input("Enter the growth rate of the city (e.g. 123 or 123.4): "))
            break
        except ValueError:
            print(
                "Invalid input. Growth rate must be a number.\n")

    return growth