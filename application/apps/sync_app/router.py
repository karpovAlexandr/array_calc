from fastapi import APIRouter

from calculation import short_calculations
from config import ARRAY_KEY_NAME
from schemas import ArrayDataIn, ArrayDataOut

router = APIRouter(prefix="/sync")


@router.post("", response_model=ArrayDataOut)
def sync_calculate(data: ArrayDataIn):
    """
    Synchronous array calculator
    :param data:  array data
    :return: ArrayDataOut schema
    """
    return ArrayDataOut(result=short_calculations(getattr(data, ARRAY_KEY_NAME)))
