import datetime
from typing import Optional, List

import pydantic

from features.recipes.instructions.responses import InstructionResponse


class BaseRecipeResponse(pydantic.BaseModel):
    status_code: int
    text: str


class Category(pydantic.BaseModel):
    """Category response"""
    id: int
    name: str
    created_by: str
    created_on: datetime.datetime
    updated_by: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None


class RecipeResponse(pydantic.BaseModel):
    """Recipe response"""
    id: int
    name: str
    picture: str
    summary: str
    carbo: Optional[float] = None
    fats: Optional[float] = None
    proteins: Optional[float] = None
    cholesterol: Optional[float] = None
    time_to_prepare: int
    complexity: float
    created_by: str
    created_on: datetime.datetime
    updated_by: Optional[str] = None
    updated_on: Optional[datetime.datetime] = None
    category_id: int
    instructions: Optional[List[InstructionResponse]] = None
    # instructions: str
    # instructions: Mapped[list["RecipeInstruction"]] = relationship("RecipeInstruction", back_populates="recipe",
    #                                                                init=False)
