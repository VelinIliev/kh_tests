from typing import Type

from features.recipes.models import RecipeCategory
import db.connection


def get_all_categories() -> list[Type[RecipeCategory]]:
    with db.connection.get_session() as session:
        return session.query(RecipeCategory).all()


