from time import sleep

from dals.result import ResultDAL
from db import async_session
from schemas import SessionIdIn


async def async_calculate(session_id: str, nums: list[int]) -> None:
    async with async_session() as session:
        async with session.begin():
            schema = SessionIdIn(session_id=session_id)
            result_dal = ResultDAL(session)
            await result_dal.create(schema)
    sleep(5)
    result = sum(nums)
    sleep(5)
    async with async_session() as session:
        async with session.begin():
            return await result_dal.update(session_id, result=result)
