from pydantic import BaseModel

class FlightSearch(BaseModel):
    origin: str
    destination: str
    departure_date: str
    return_date: str

class FlightResult(BaseModel):
    id: str
    origin: str
    destination: str
    departure_date: str
    return_date: str
    price: float