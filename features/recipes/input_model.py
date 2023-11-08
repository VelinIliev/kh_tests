from pydantic import BaseModel, Field


class RecipeInput(BaseModel):
    name: str = Field(max_length=255)
    picture: str = Field(max_length=255)
    summary: str = Field(max_length=1000)
    calories: float = Field()
    carbo: float = Field()
    fats: float = Field()
    proteins: float = Field()
    cholesterol: float = Field()
    time_to_prepare: int = Field()
    created_by: str = Field(max_length=30)
    updated_by: str = Field(max_length=30)
