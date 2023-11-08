import fastapi
from starlette import status

from db.connection import get_session
from .operations import fetch_all_instructions, dump_create_instructions
from features.recipes.models import RecipeInstruction, Recipe
from features.recipes.instructions.input_models import InstructionInput, InstructionRequest
from .responses import InstructionResponse
from ...health.responses import BaseHealthResponse

router = fastapi.APIRouter()


@router.get('/', )
def get_all_instructions():
    instructions = fetch_all_instructions()
    return [InstructionResponse(**_.__dict__) for _ in instructions]


@router.post('/')
def create_instruction(instructions_request: InstructionRequest, recipe_id: int):

    dump_create_instructions(instructions_request, recipe_id)

    return BaseHealthResponse(status_code=status.HTTP_201_CREATED, text='instructions created')
