from typing import Optional

from pydantic import BaseModel, Field


class ArrayDataOut(BaseModel):
    result: Optional[int] = Field(title="calculation's result", default=None)


class SessionIdIn(BaseModel):
    session_id: str = Field(title="task's session id")


class SessionIdOut(SessionIdIn):
    ...


class ArrayDataIn(BaseModel):
    array: list[int] = Field(list(), title="array of numbers to sum")
