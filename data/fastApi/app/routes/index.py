from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def index():
    """
    `목차`\n
    """
    return {"about": {
        "/": "about",
        "/data/openApi": "openApi parsing",
        "/data/naverApi": "naverApi parsing",
        "/recommand/latent/{id}": "latent filtering",
        "/recommand/predict/{id}": "linear Regression",
    }}
