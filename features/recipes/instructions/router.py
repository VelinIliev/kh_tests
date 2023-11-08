import fastapi

from db.connection import get_session
from features.recipes.models import RecipeInstruction, Recipe
from features.recipes.instructions.input_models import InstructionInput, InstructionRequest

router = fastapi.APIRouter()


@router.get('/', )
def api_recipes():
    """API health"""
    return "instructions"


@router.post('/')
def create_instruction(instructions_request: InstructionRequest, recipe_id: int):
    db = get_session()

    instructions = instructions_request.instructions
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    total_complexity = 0
    for instruction in instructions:
        new_instruction = RecipeInstruction(**instruction.model_dump())
        new_instruction.recipe_id = recipe_id
        total_complexity += new_instruction.complexity
        db.add(new_instruction)
        db.commit()

    recipe.complexity = round(total_complexity / len(instructions), 1)
    db.add(recipe)
    db.commit()
