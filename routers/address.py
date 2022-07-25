from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import address_services
from schemas.schema import (Address, AddressResponse, GetAddress, ResponseCommonMessage)
import models


app = APIRouter(prefix="/v1/be", tags=["ADDRESS BOOK"])


@app.post("/address")
def create_address(
    payload: Address,
    db: Session = Depends(get_db)
):
    response = address_services.create_address(payload, db)
    return response


@app.get("/address")
def get_id(
    id: str,
    db: Session = Depends(get_db)
):
    response = address_services.get_address(id,db)
    return response


@app.delete("/address")
def delete_address(
    id: str,
    db: Session = Depends(get_db)
):
    response = address_services.delete_address(id, db)
    return response


@app.put("/address")
def update_address(
    payload: AddressResponse,
    db: Session = Depends(get_db)
):
    response = address_services.update_address(payload, db)
    return response
    


@app.post("/address/retrieve")
def get_address(
    payload: GetAddress,
    db: Session = Depends(get_db)
):
    response = address_services.retrieve_address(payload, db)
    return response
    

@app.get("/all")
def get_all(db: Session = Depends(get_db)):
    address = db.query(models.Address).all()
    return {"data": address}
