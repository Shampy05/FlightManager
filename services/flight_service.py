# flight_service.py
from sqlalchemy.orm import Session
from db.session import Session
from db.models.flight import Flight

class FlightService:
    def __init__(self, session: Session):
        self.session = session

    def add_flight(self, flight_data):
        """
        Add a new flight to the database.
        """
        flight = Flight(**flight_data)
        self.session.add(flight)
        self.session.commit()

    def get_flight(self, flight_id):
        """
        Retrieve a flight by its ID.
        """
        return self.session.query(Flight).filter_by(id=flight_id).first()

    def update_flight(self, flight_id, update_data):
        """
        Update a flight's data.
        """
        flight = self.get_flight(flight_id)
        for key, value in update_data.items():
            setattr(flight, key, value)
        self.session.commit()

    def delete_flight(self, flight_id):
        """
        Delete a flight by its ID.
        """
        flight = self.get_flight(flight_id)
        self.session.delete(flight)
        self.session.commit()

    def search_flights(self, **filters):
        """
        Search for flights based on filters.
        """
        return self.session.query(Flight).filter_by(**filters).all()

    def get_flights_by_aircraft(self, aircraft_id):
        """
        Get all flights for a specific aircraft.
        """
        return self.session.query(Flight).filter_by(aircraft_id=aircraft_id).all()

    def get_flights_by_pilot(self, pilot_id):
        """
        Get all flights conducted by a specific pilot.
        """
        # Assuming there is a many-to-many relation between Flight and Pilot 
        # and flight_pilots table in the database handles this relation
        return self.session.query(Flight).filter(Flight.pilots.any(id=pilot_id)).all()
