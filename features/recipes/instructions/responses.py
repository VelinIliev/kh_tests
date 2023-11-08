from pydantic import BaseModel


class InstructionResponse(BaseModel):
    instruction: str
    category: str
    time: int
    complexity: float