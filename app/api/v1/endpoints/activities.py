from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_activities():
    return {"message": "Get activity history endpoint - to be implemented"}

@router.post("/sync")
async def sync_external_data():
    return {"message": "Sync external fitness data endpoint - to be implemented"}

@router.get("/analytics/progress")
async def get_progress_analytics():
    return {"message": "Get progress analytics endpoint - to be implemented"}