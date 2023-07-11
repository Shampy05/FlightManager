from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

# Association Table
pilot_flight = Table('pilot_flight', Base.metadata,
    Column('pilot_id', Integer, ForeignKey('pilots.id')),
    Column('flight_id', Integer, ForeignKey('flights.id'))
)

class Pilot(Base):
    __tablename__ = 'pilots'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship to flights
    flights = relationship("Flight", secondary=pilot_flight, back_populates="pilots")

    def __repr__(self):
        return f"<Pilot(id={self.id}, name='{self.name}')>"
