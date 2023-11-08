import db.connection
from .instructions.responses import InstructionResponse
from .models import RecipeCategory, Recipe, RecipeInstruction
from typing import Type


def get_all_recipes() -> list[Type[Recipe]]:
    with db.connection.get_session() as session:
        return session.query(Recipe).all()
