from pydantic import BaseModel


class ResponseCommonMessage(BaseModel):
    status: str
    message: str
    

class Address(BaseModel):
    address:str

class AddressResponse(BaseModel):
    id:str
    address:str
    api_address:str
    latitude:str
    longitude:str


class Coordinates(BaseModel):
    latitude: float
    longitude: float
    
class GetAddress(BaseModel):
    distance: float
    coordinates: Coordinates