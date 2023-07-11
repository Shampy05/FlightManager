# aircraft_service.py
from sqlalchemy.orm import Session
from db.session import Session
from db.models.aircraft import Aircraft

class AircraftService:
    def __init__(self, session: Session):
        self.session = session

    def add_aircraft(self, aircraft_data):
        """
        Add a new aircraft to the database.
        """
        aircraft = Aircraft(**aircraft_data)
        self.session.add(aircraft)
        self.session.commit()

    def get_aircraft(self, aircraft_id):
        """
        Retrieve an aircraft by its ID.
        """
        return self.session.query(Aircraft).filter_by(id=aircraft_id).first()

    def update_aircraft(self, aircraft_id, update_data):
        """
        Update an aircraft's data.
        """
        aircraft = self.get_aircraft(aircraft_id)
        for key, value in update_data.items():
            setattr(aircraft, key, value)
        self.session.commit()

    def delete_aircraft(self, aircraft_id):
        """
        Delete an aircraft by its ID.
        """
        aircraft = self.get_aircraft(aircraft_id)
        self.session.delete(aircraft)
        self.session.commit()

    def search_aircrafts(self, **filters):
        """
        Search for aircraft based on filters.
        """
        return self.session.query(Aircraft).filter_by(**filters).all()
