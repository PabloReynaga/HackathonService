from fastapi import APIRouter, HTTPException
from app.services.vector_db import VectorDBService
from app.models.vector import VectorRequest, VectorResponse

router = APIRouter()
vector_service = VectorDBService()

@router.post("/add-vector", response_model=VectorResponse)
def add_vector(request: VectorRequest):
    try:
        vector_id = vector_service.add_vector(request.vector)
        return VectorResponse(id=vector_id, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
