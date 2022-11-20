from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class JornalURL(Base):
    __tablename__ = "jornal_url"

    name = Column('name', String, nullable=False)
    description = Column('description', String, nullable=False)
    url = Column('url', String, nullable=False, primary_key=True)
    timestamp = Column('date_tsmp', DateTime, nullable=False)
    date = Column('date_str', String, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    path = Column('path', String, nullable=False)
    colors = Column('colors', String, nullable=False)
    colors_simple = Column('colors_simple', String, nullable=False)