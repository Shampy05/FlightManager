from sqlalchemy import Column, Integer, String 
from db.base import Base
from sqlalchemy.orm import relationship

class Aircraft(Base):
    __tablename__ = 'aircrafts'

    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    model = Column(String, nullable=False)
    capacity=Column(Integer, nullable=False)

    flights = relationship("Flight", back_populates="aircraft")

    def __repr__(self):
        return f"<Aircraft(id={self.id}, name={self.name}, model={self.model}, capacity={self.capacity})"