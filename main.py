from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int

class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

stations = [
    {
        "id": 1,
        "name": "МКС",
        "orbit": "Низкая околоземная орбита",
        "crew": 7
    },
    {
        "id": 2,
        "name": "Тяньгун",
        "orbit": "Низкая околоземная орбита",
        "crew": 3
    }
]

@app.get("/stations", response_model=list[Station])
def get_stations():
    return stations

@app.post("/stations", response_model=Station, status_code=201)
def create_station(station_data: StationCreate):
    new_id = len(stations) + 1
    new_station = {
        "id": new_id,
        "name": station_data.name,
        "orbit": station_data.orbit,
        "crew": station_data.crew
    }
    stations.append(new_station)
    return new_station