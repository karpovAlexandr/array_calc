from fastapi import APIRouter, BackgroundTasks, HTTPException, Response, status

from apps.async_app.tasks import async_calculate_task
from apps.async_app.utils import generate_str_uuid
from config import ARRAY_KEY_NAME
from dals import ResultDAL
from db import async_session
from schemas import ArrayDataIn, ArrayDataOut, SessionIdOut

router = APIRouter(prefix="/async")


@router.post("", response_model=SessionIdOut)
async def async_calculate(data: ArrayDataIn, background_tasks: BackgroundTasks):
    """
    Asynchronous array calculator
    :param data: array data
    :return: SessionIdOut schema
    """
    nums: list = getattr(data, ARRAY_KEY_NAME)
    session_id: str = generate_str_uuid()
    background_tasks.add_task(async_calculate_task, session_id, nums)
    return SessionIdOut(session_id=session_id)


@router.get(
    "/{session_id}",
    response_model=ArrayDataOut,
    responses={404: {"model": ArrayDataOut}, 204: {}},
)
async def get_result(session_id: str, response: Response):
    """
    Get result by session's id
    :param session_id: calculation session's id
    :return: ArrayDataOut schema
    """
    async with async_session() as session:
        async with session.begin():
            result_dal = ResultDAL(session)
            result = await result_dal.get(session_id)

            if not result:
                raise HTTPException(404, "No such session")

            if not result.result:
                response.status_code = status.HTTP_204_NO_CONTENT

    return ArrayDataOut(result=result.result)
