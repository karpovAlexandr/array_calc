from fastapi import APIRouter, BackgroundTasks

from apps.async_app.tasks import async_calculate
from apps.async_app.utils import generate_str_uuid
from config import ARRAY_KEY_NAME
from schemas import ArrayDataIn, ArrayDataOut, SessionIdOut
from dals.result import ResultDAL
from db import async_session

router = APIRouter(prefix="/async")


@router.post("", response_model=SessionIdOut)
async def calculate(data: ArrayDataIn, background_tasks: BackgroundTasks):
    nums: list = getattr(data, ARRAY_KEY_NAME)
    session_id: str = generate_str_uuid()
    background_tasks.add_task(async_calculate, session_id, nums)
    return SessionIdOut(session_id=session_id)


@router.get("/{session_id}", response_model=ArrayDataOut)
async def get_result(session_id: str):
    async with async_session() as session:
        async with session.begin():
            result_dal = ResultDAL(session)
            result = await result_dal.get(session_id)
            if not result:
                raise

            if not result.result:
                raise

    return ArrayDataOut(result=result.result)
