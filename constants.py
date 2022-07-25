import schemas
from fastapi import status

common_msg = schemas.ResponseCommonMessage(status=status.HTTP_200_OK, message="success")