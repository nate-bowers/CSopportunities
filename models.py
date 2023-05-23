"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "events"

    # Columns
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    name = Column("name", TEXT)
    link = Column("link", TEXT)
    summary = Column("summary", TEXT)
    organization = Column("organization", TEXT)
    price = Column("price", TEXT)
    online = Column("online", Boolean)
    location = Column("location", TEXT)
    image_address = Column("image_address", TEXT)
    age_high = Column("age_high", INTEGER)
    age_low = Column("age_low", INTEGER)
    event_type = Column("event_type", TEXT)
    during_school_year = Column("during_school_year", Boolean)
    length = Column("length", TEXT)
