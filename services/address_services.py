from fastapi import status
from sqlalchemy.orm import Session
from utility import coordinates
from schemas.schema import Address, AddressResponse, GetAddress, ResponseCommonMessage
import models
from uuid import uuid4


def get_uuid():
    return str(uuid4())


def create_address(payload, db:Session):
    
    """
    This api adds a new address in the Address Book.

    Parameters
    ----------
    address : String containing address to be added

    Returns
        Returns address entered along with its coordinates fetched by google api.
    -------

    """
    
    id = get_uuid()
    address_detail = coordinates.getCoordinates(payload.address)
    if address_detail["status"] == "ZERO_RESULTS":
        common_msg = ResponseCommonMessage(status=status.HTTP_404_NOT_FOUND, message="Please try again with more specific address!!")
        return common_msg
    
    api_address = address_detail['results'][0]['formatted_address']
    coordinate =  address_detail['results'][0]['geometry']['location']
    
    address_exist =  db.query(models.Address).filter(models.Address.api_address == api_address).first()
    if address_exist:
        common_msg = ResponseCommonMessage(status=status.HTTP_208_ALREADY_REPORTED, message="Address already existed!")
        return common_msg
    
    user =  models.Address(id=id, address=payload.address, api_address=api_address, latitude = str(coordinate['lat']), longitude = str(coordinate['lng']))    
    db.add(user)
    db.commit()
    db.refresh(user)

    return AddressResponse(id=user.id, address=user.address, api_address = user.api_address, latitude=user.latitude, longitude = user.longitude)


def get_address(id, db:Session):
    """
    This api fetches the desired address from address book

    Parameters
    ----------
    id : id associated with that address in the address book

    Returns
        Returns desired address along with its coordinates fetched by google api.
    -------

    """
    address = db.query(models.Address).filter(models.Address.id == id).first()
    if not address:
        common_msg = ResponseCommonMessage(
            status=status.HTTP_404_NOT_FOUND, message="Address Id not found!!"
        )
        return common_msg
    return AddressResponse(
        id=address.id,
        address=address.address,
        api_address=address.api_address,
        latitude=address.latitude,
        longitude=address.longitude,
    )


def delete_address(id, db:Session):
    """
    This api deletes the desired address from address book

    Parameters
    ----------
    id : id associated with that address in the address book

    Returns
        Returns A successfully deleted message.
    -------

    """
    address_exist = db.query(models.Address).filter(models.Address.id == id)

    if not address_exist.first():
        common_msg = ResponseCommonMessage(
            status=status.HTTP_404_NOT_FOUND, message="Address Id not found!!"
        )
        return common_msg

    db.query(models.Address).filter(models.Address.id == id).delete(
        synchronize_session=False
    )
    db.commit()

    return ResponseCommonMessage(
        status=status.HTTP_200_OK, message=f"Address ID({id}) deleted successfully."
    )
    

def update_address(payload, db:Session):
    """
    This api updates the desired address from address book

    Parameters
    ----------
    id: str, address id to be modified
    address: str, new address
    api_address: str
    latitude: str
    longitude: str

    Returns
        Returns updated address.
    -------

    """
    address_data = db.query(models.Address).filter(models.Address.id == payload.id)

    if not address_data.first():
        common_msg = ResponseCommonMessage(
            status=status.HTTP_404_NOT_FOUND, message="Address Id not found!!"
        )
        return common_msg

    address_data.update(
        {
            "address": payload.address,
            "latitude": payload.latitude,
            "longitude": payload.longitude,
        },
        synchronize_session=False,
    )
    db.commit()
    db.refresh(address_data.first())

    return address_data.first()


def retrieve_address(payload, db:Session):
    """
    This api fetches all address in address book present in vicinity of the entered location

    Parameters
    ----------
    distance : It has to passed in KM, associated with that address in the address book.
    latitude: origin latitude from which the distance to be measured.
    longitude: origin longitude from which the distance to be measured.

    Returns
        Returns desired addresses along with its coordinates fetched by google api.
    -------

    """
    address_data = db.query(models.Address).all()
    address_list = list()

    for address in address_data:
        if (
            coordinates.get_distance(
                payload.coordinates.latitude,
                float(address.latitude),
                payload.coordinates.longitude,
                float(address.longitude),
            )
            <= payload.distance
        ):
            address_list.append(
                AddressResponse(
                    id=address.id,
                    address=address.address,
                    api_address=address.api_address,
                    latitude=address.latitude,
                    longitude=address.longitude,
                )
            )

    return address_list