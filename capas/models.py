from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class JornalURL(Base):
    __tablename__ = "jornal_url"

    id = Column('id', Integer, primary_key=True, index=True)
    jornal_name = Column('jornal_name', String, nullable=False)
    description = Column('description', String, nullable=False)
    image_url = Column('image_url', String, nullable=False)
    timestamp = Column('date_tsmp', DateTime, nullable=False)
    date = Column('date_str', String, nullable=False)
    created = Column('created', DateTime, nullable=False)