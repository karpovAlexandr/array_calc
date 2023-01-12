from typing import Union

from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from models import Result
from schemas import SessionIdIn


class ResultDAL:
    model = Result
    fields_to_update = ("result",)

    def __init__(self, db_session: "Session") -> None:
        self.session = db_session

    async def get(self, session_id: str) -> Union[None, "ResultDAL.model"]:
        results: "ChunkedIteratorResult" = await self.session.execute(
            select(self.model).where(self.model.session_id == session_id)
        )
        result = results.one_or_none()
        return result[0] if result else result

    async def create(self, schema_instance: SessionIdIn) -> "Result":
        instance = self.model(**schema_instance.dict())
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def update(self, session_id: str, **kwargs) -> "Result":
        instance: "Result" = await self.get(session_id)
        for attr, value in kwargs.items():
            if attr in ResultDAL.fields_to_update:
                setattr(instance, attr, value)
        self.session.add(instance)
        await self.session.commit()
        return instance
