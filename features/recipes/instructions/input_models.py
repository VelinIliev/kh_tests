from typing import List

from pydantic import BaseModel, Field


class InstructionInput(BaseModel):
    instruction: str = Field(max_length=300)
    category: str = Field(max_length=100)
    time: int = Field()
    complexity: float = Field()


class InstructionRequest(BaseModel):
    instructions: List[InstructionInput]
