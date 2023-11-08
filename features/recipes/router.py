import fastapi

import features
import features.recipes.operations as op
import features.recipes.responses
from db.connection import get_session
from features.recipes.categories import router as categories_router
from features.recipes.instructions import router as instructions_router
from .models import Recipe

router = fastapi.APIRouter()

router.include_router(instructions_router, prefix="/instructions", tags=["Instructions"])
router.include_router(categories_router, prefix="/categories", tags=["Categories"])


# @router.get('/', )
# def get_all_recipes():
#     db = get_session()
#     recipes_x = db.query(Recipe).all()
#     return recipes_x


@router.get('/')
def get_all_categories():
    """
    Get all categories
    :return:
    """

    categories = op.get_all_recipe_categories()

    return [features.recipes.responses.Category(**_.__dict__) for _ in categories]

# @router.post('/')
# def create_recipe(recipe_request: RecipeInput, category_request: int):
#     db = get_session()
#     category = db.query(RecipeCategory).filter(RecipeCategory.id == category_request).first()
#     recipe = Recipe(**recipe_request.model_dump())
#     recipe.category = category
#     db.add(recipe)
#     db.commit()
#
#     return BaseRecipeResponse(status_code=status.HTTP_204_NO_CONTENT, text='Recipe created')
