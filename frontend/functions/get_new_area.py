def get_new_area():
    """
    Function to get the area of a city from the user and validate it
    """

    while True:
        try:
            area = float(
                input("Enter the area of the city in kilometers squared: "))

            if area < 0:
                print('Invalid input: A city can not have a negative area')
            elif area == 0:
                print('Invalid input: A city can not have an area of 0')
            else:
                break

        except ValueError:
            print(
                "Invalid input. Area must be a number.\n")

    return area