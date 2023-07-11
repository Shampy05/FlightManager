# utils.statistics.py
from sqlalchemy.orm import Session
from db.session import Session
from db.models.flight import Flight
from sqlalchemy import func, extract

class FlightStatistics:
    def __init__(self, session: Session):
        self.session = session

    def get_flights_per_week(self, year, week):
        """
        Return the number of flights in a specific week of a specific year.
        """
        return self.session.query(Flight).filter(
            extract('year', Flight.date) == year,
            extract('week', Flight.date) == week).count()

    def get_flights_to_destination_per_month(self, year, month, destination):
        """
        Return the number of flights to a specific destination in a specific month of a specific year.
        """
        return self.session.query(Flight).filter(
            Flight.destination == destination,
            extract('year', Flight.date) == year,
            extract('month', Flight.date) == month).count()
