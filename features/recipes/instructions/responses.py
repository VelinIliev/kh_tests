from pydantic import BaseModel


class InstructionResponse(BaseModel):
    id: int
    instruction: str
    category: str
    time: int
    complexity: float
