from typing import Type

from fastapi import HTTPException

from db.connection import get_session
from features.recipes.instructions.responses import InstructionResponse
from features.recipes.models import RecipeInstruction, Recipe


def fetch_all_instructions() -> list[Type[RecipeInstruction]]:
    with get_session() as session:
        return session.query(RecipeInstruction).all()


def create_instructions_and_calculate_time_and_complexity(instructions_request, recipe_id):
    db = get_session()

    instructions = instructions_request.instructions

    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    old_instructions = db.query(RecipeInstruction).filter(RecipeInstruction.recipe_id == recipe_id)

    old_total = (sum([InstructionResponse(**x.__dict__).complexity for x in old_instructions]))
    old_len = (len([InstructionResponse(**x.__dict__).complexity for x in old_instructions]))
    old_time_to_prepare = (sum([InstructionResponse(**x.__dict__).time for x in old_instructions]))

    total_complexity = old_total
    total_time_to_prepare = old_time_to_prepare

    for instruction in instructions:
        new_instruction = RecipeInstruction(**instruction.model_dump())
        new_instruction.recipe_id = recipe_id
        total_time_to_prepare += new_instruction.time
        total_complexity += new_instruction.complexity
        db.add(new_instruction)
        db.commit()

    recipe.complexity = round(total_complexity / (len(instructions) + old_len), 1)
    recipe.time_to_prepare = total_time_to_prepare
    db.add(recipe)
    db.commit()
    db.close()
