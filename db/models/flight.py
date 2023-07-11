from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base
from db.models.pilot import pilot_flight

class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False, unique=True)
    destination = Column(String, nullable=False)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'))
    
    pilots = relationship("Pilot", secondary=pilot_flight, back_populates="flights")

    # Relationship to aircraft
    aircraft = relationship("Aircraft", back_populates="flights")

    def __repr__(self):
        return f"<Flight(id={self.id}, number='{self.number}', destination='{self.destination}', aircraft_id={self.aircraft_id})>"
