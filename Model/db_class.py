from sqlalchemy import Column, TEXT, BOOLEAN , BIGINT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(BIGINT,nullable=False, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    completed = Column(BOOLEAN, nullable=False)


