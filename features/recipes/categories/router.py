import fastapi
from fastapi import HTTPException
from starlette import status

from .input_model import CategoryRequest, CategoryUpdateRequest
# from db.connection import get_session
# from features.recipes.models import RecipeCategory
# from features.recipes.categories import operations, responses
# import features.recipes.categories
# from features.recipes.models import RecipeCategory
from .operations import get_all_categories
from .responses import CategoryResponse
from db.connection import get_session
from features.recipes.models import RecipeCategory
from features.health.responses import BaseHealthResponse

router = fastapi.APIRouter()


@router.get('/')
def category_get_all():
    categories = get_all_categories()
    return [CategoryResponse(**_.__dict__) for _ in categories]


@router.post('/create')
def category_create(category_request: CategoryRequest):
    db = get_session()
    category = RecipeCategory(**category_request.model_dump())
    db.add(category)
    db.commit()
    db.close()
    return BaseHealthResponse(status_code=status.HTTP_201_CREATED, text="Category created")


@router.put('/{category_id}')
def category_update(category_id: int, category_request: CategoryUpdateRequest):
    db = get_session()
    category = db.query(RecipeCategory).filter(RecipeCategory.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = category_request.name
    category.updated_by = category_request.updated_by

    db.add(category)
    db.commit()
    db.close()

    return BaseHealthResponse(status_code=status.HTTP_204_NO_CONTENT, text="Category updated")


@router.delete('/{category_id}')
def category_delete(category_id: int):
    db = get_session()
    category = db.query(RecipeCategory).filter(RecipeCategory.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    db.close()

    return BaseHealthResponse(status_code=status.HTTP_204_NO_CONTENT, text="Category deleted")
