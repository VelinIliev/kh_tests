import datetime

from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_on: datetime.datetime
    created_by: str
    updated_on: datetime.datetime
    updated_by: str
