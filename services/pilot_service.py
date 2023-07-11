# pilot_service.py
from sqlalchemy.orm import Session
from db.session import Session
from db.models.pilot import Pilot

class PilotService:
    def __init__(self, session: Session):
        self.session = session

    def add_pilot(self, pilot_data):
        """
        Add a new pilot to the database.
        """
        pilot = Pilot(**pilot_data)
        self.session.add(pilot)
        self.session.commit()

    def get_pilot(self, pilot_id):
        """
        Retrieve a pilot by their ID.
        """
        return self.session.query(Pilot).filter_by(id=pilot_id).first()

    def update_pilot(self, pilot_id, update_data):
        """
        Update a pilot's data.
        """
        pilot = self.get_pilot(pilot_id)
        for key, value in update_data.items():
            setattr(pilot, key, value)
        self.session.commit()

    def delete_pilot(self, pilot_id):
        """
        Delete a pilot by their ID.
        """
        pilot = self.get_pilot(pilot_id)
        self.session.delete(pilot)
        self.session.commit()

    def search_pilots(self, **filters):
        """
        Search for pilots based on filters.
        """
        return self.session.query(Pilot).filter_by(**filters).all()

    def get_pilots_by_flight(self, flight_id):
        """
        Get all pilots for a specific flight.
        """
        # Assuming there is a many-to-many relation between Flight and Pilot 
        # and flight_pilots table in the database handles this relation
        return self.session.query(Pilot).filter(Pilot.flights.any(id=flight_id)).all()
