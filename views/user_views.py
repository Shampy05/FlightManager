# views/user_views.py
from db.session import Session
from services.aircraft_service import AircraftService
from services.flight_service import FlightService
from services.pilot_service import PilotService
from utils.statistics import FlightStatistics

def main_menu():
    """
    Display the main menu to the user and handle their selection.
    """
    print("\n--- Main Menu ---")
    print("1. Manage Aircrafts")
    print("2. Manage Flights")
    print("3. Manage Pilots")
    print("4. View Statistics")
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
        print("Goodbye!")
    else:
        print("Invalid selection. Please try again.")
        main_menu()

def aircraft_menu():
    """
    Display the aircraft menu to the user and handle their selection.
    """
    print("\n--- Aircraft Menu ---")
    print("1. Add Aircraft")
    print("2. Update Aircraft")
    print("3. Delete Aircraft")
    print("4. View All Aircrafts")
    print("5. Return to Main Menu")

    selection = input("Please enter your selection: ")
    aircraft_service = AircraftService(Session())

    if selection == "1":
        id = input("Enter aircraft id: ")
        model = input("Enter aircraft model: ")
        aircraft_service.add_aircraft(id, model)
        print("Aircraft added successfully.")
    elif selection == "2":
        id = input("Enter aircraft id to update: ")
        model = input("Enter new aircraft model: ")
        aircraft_service.update_aircraft(id, model)
        print("Aircraft updated successfully.")
    elif selection == "3":
        id = input("Enter aircraft id to delete: ")
        aircraft_service.delete_aircraft(id)
        print("Aircraft deleted successfully.")
    elif selection == "4":
        aircrafts = aircraft_service.get_all_aircrafts()
        for aircraft in aircrafts:
            print(f"ID: {aircraft.id}, Model: {aircraft.model}")
    elif selection == "5":
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        aircraft_menu()


def flight_menu():
    """
    Display the flight menu to the user and handle their selection.
    """
    print("\n--- Flight Menu ---")
    print("1. Add Flight")
    print("2. Update Flight")
    print("3. Delete Flight")
    print("4. View All Flights")
    print("5. Return to Main Menu")

    selection = input("Please enter your selection: ")
    flight_service = FlightService(Session())

    if selection == "1":
        id = input("Enter flight id: ")
        destination = input("Enter flight destination: ")
        aircraft_id = input("Enter aircraft id for the flight: ")
        flight_service.add_flight(id, destination, aircraft_id)
        print("Flight added successfully.")
    elif selection == "2":
        id = input("Enter flight id to update: ")
        destination = input("Enter new flight destination: ")
        aircraft_id = input("Enter new aircraft id for the flight: ")
        flight_service.update_flight(id, destination, aircraft_id)
        print("Flight updated successfully.")
    elif selection == "3":
        id = input("Enter flight id to delete: ")
        flight_service.delete_flight(id)
        print("Flight deleted successfully.")
    elif selection == "4":
        flights = flight_service.get_all_flights()
        for flight in flights:
            print(f"ID: {flight.id}, Destination: {flight.destination}, Aircraft ID: {flight.aircraft_id}")
    elif selection == "5":
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        flight_menu()


def pilot_menu():
    """
    Display the pilot menu to the user and handle their selection.
    """
    print("\n--- Pilot Menu ---")
    print("1. Add Pilot")
    print("2. Update Pilot")
    print("3. Delete Pilot")
    print("4. View All Pilots")
    print("5. Return to Main Menu")

    selection = input("Please enter your selection: ")
    pilot_service = PilotService(Session())

    if selection == "1":
        id = input("Enter pilot id: ")
        name = input("Enter pilot name: ")
        pilot_service.add_pilot(id, name)
        print("Pilot added successfully.")
    elif selection == "2":
        id = input("Enter pilot id to update: ")
        name = input("Enter new pilot name: ")
        pilot_service.update_pilot(id, name)
        print("Pilot updated successfully.")
    elif selection == "3":
        id = input("Enter pilot id to delete: ")
        pilot_service.delete_pilot(id)
        print("Pilot deleted successfully.")
    elif selection == "4":
        pilots = pilot_service.get_all_pilots()
        for pilot in pilots:
            print(f"ID: {pilot.id}, Name: {pilot.name}")
    elif selection == "5":
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        pilot_menu()


def statistics_menu():
    """
    Display the statistics menu to the user and handle their selection.
    """
    print("\n--- Statistics Menu ---")
    print("1. View Flights Per Week")
    print("2. View Flights To Destination Per Month")
    print("3. Return to Main Menu")

    selection = input("Please enter your selection: ")
    stats_service = FlightStatistics(Session())

    if selection == "1":
        flights = stats_service.get_flights_per_week()
        for flight in flights:
            print(f"Week: {flight['week']}, Number of flights: {flight['flights_count']}")
    elif selection == "2":
        destination = input("Enter destination: ")
        month = input("Enter month (1-12): ")
        flights = stats_service.get_flights_to_destination_per_month(destination, month)
        print(f"Number of flights to {destination} in month {month}: {flights}")
    elif selection == "3":
        main_menu()
    else:
        print("Invalid selection. Please try again.")
        statistics_menu()

if __name__ == "__main__":
    # If this script is run directly, display the main menu
    main_menu()
