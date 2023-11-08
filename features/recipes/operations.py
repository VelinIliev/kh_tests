import db.connection
from .instructions.responses import InstructionResponse
from .models import RecipeCategory, Recipe, RecipeInstruction
from typing import Type


def get_all_recipes() -> list[Type[Recipe]]:
    """
    Get all recipes
    :return:
    """
    with db.connection.get_session() as session:
        return session.query(Recipe).all()
