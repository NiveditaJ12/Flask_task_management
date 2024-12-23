from sqlalchemy import Integer, String, Column, Enum
from config import Base
import enum

class StatusList(enum.Enum):
    done = 'Done'
    unfinished = 'Unfinished'
    postpone = 'Postponed'
    cancelled = 'Cancelled'

class ToDo(Base):
    __tablename__ = 'ToDo'
    id = Column(Integer, primary_key = True)
    sr_no = Column(Integer)
    task = Column(String(50), nullable=True, unique=True)
    status = Column(Enum(StatusList), nullable = True)
