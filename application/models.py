from sqlalchemy import Column, Integer, String

from db import Base


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String)
    result = Column(Integer, default=None)
