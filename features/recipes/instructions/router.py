import fastapi
from starlette import status

from features.recipes.instructions.input_models import InstructionRequest
from .operations import fetch_all_instructions, create_instructions_and_calculate_time_and_complexity
from .responses import InstructionResponse
from ...health.responses import BaseHealthResponse

router = fastapi.APIRouter()


@router.get('/', )
def get_all_instructions():
    instructions = fetch_all_instructions()
    return [InstructionResponse(**i.__dict__) for i in instructions]


@router.post('/')
def create_instruction(instructions_request: InstructionRequest, recipe_id: int):
    create_instructions_and_calculate_time_and_complexity(instructions_request, recipe_id)

    return BaseHealthResponse(status_code=status.HTTP_201_CREATED, text='instructions created')
