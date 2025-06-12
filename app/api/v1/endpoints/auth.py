from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    return {"message": "User registration endpoint - to be implemented"}

@router.post("/login")
async def login():
    return {"message": "User login endpoint - to be implemented"}

@router.post("/refresh")
async def refresh_token():
    return {"message": "Token refresh endpoint - to be implemented"}