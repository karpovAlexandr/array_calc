from fastapi import APIRouter

from config import ARRAY_KEY_NAME
from schemas import ArrayDataIn, ArrayDataOut

router = APIRouter(prefix="/sync")


@router.post("", response_model=ArrayDataOut)
def calculate(data: ArrayDataIn):
    return ArrayDataOut(result=sum(getattr(data, ARRAY_KEY_NAME)))
