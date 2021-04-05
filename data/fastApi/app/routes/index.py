import datetime
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"about": {
        "/": "about",
        "/open": "open API parsing"
    }}
