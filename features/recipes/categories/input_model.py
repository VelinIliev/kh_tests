from pydantic import BaseModel, Field


class CategoryRequest(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    created_by: str = Field(max_length=30)
    updated_by: str = Field(max_length=30)


class CategoryUpdateRequest(BaseModel):
    name: str = Field(max_length=50)
    updated_by: str = Field(max_length=30)
