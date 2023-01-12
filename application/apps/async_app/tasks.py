from calculation import long_async_calculations
from dals import ResultDAL
from db import async_session
from models import Result
from schemas import SessionIdIn


async def async_calculate_task(session_id: str, nums: list[int]) -> Result:
    async with async_session() as session:
        async with session.begin():
            schema = SessionIdIn(session_id=session_id)
            result_dal = ResultDAL(session)
            await result_dal.create(schema)

    result = await long_async_calculations(nums)

    async with async_session() as session:
        async with session.begin():
            return await result_dal.update(session_id, result=result)
