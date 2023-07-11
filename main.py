from views.user_views import aircraft_menu, flight_menu, pilot_menu, statistics_menu

def main_menu():
    """
    Display the main menu to the user and handle their selection.
    """
    print("\n--- Main Menu ---")
    print("1. Aircraft Menu")
    print("2. Flight Menu")
    print("3. Pilot Menu")
    print("4. Statistics Menu")
    print("5. Exit")

    selection = input("Please enter your selection: ")

    if selection == "1":
        aircraft_menu()
    elif selection == "2":
        flight_menu()
    elif selection == "3":
        pilot_menu()
    elif selection == "4":
        statistics_menu()
    elif selection == "5":
        print("Exiting program...")
    else:
        print("Invalid selection. Please try again.")
        main_menu()

def main():
    print("Welcome to the Airlines Flight Database Management System!")
    main_menu()

if __name__ == "__main__":
    main()
