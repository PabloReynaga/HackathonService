import fastapi
from app.services import service
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    service.search()
