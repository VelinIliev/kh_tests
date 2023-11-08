import fastapi
from fastapi import HTTPException

from db.connection import get_session
from features.health import responses
from features.recipes.categories.input_model import CategoryRequest, CategoryUpdateRequest
from features.recipes.models import RecipeCategory

router = fastapi.APIRouter()


@router.get('/')
def api_category_get_all():
    db = get_session()
    categories = db.query(RecipeCategory).all()

    return categories


@router.post('/create')
def api_category_create(category_request: CategoryRequest):
    db = get_session()
    category = RecipeCategory(**category_request.model_dump())
    db.add(category)
    db.commit()
    return responses.BaseHealthResponse(status_code=fastapi.status.HTTP_204_NO_CONTENT, text="Category created")


@router.put('/{category_id}')
def api_category_update(category_id: int, category_request: CategoryUpdateRequest):
    db = get_session()
    category = db.query(RecipeCategory).filter(RecipeCategory.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = category_request.name
    category.updated_by = category_request.updated_by

    db.add(category)
    db.commit()

    return responses.BaseHealthResponse(status_code=fastapi.status.HTTP_204_NO_CONTENT, text="Category updated")


@router.delete('/{category_id}')
def api_category_delete(category_id: int):
    db = get_session()
    category = db.query(RecipeCategory).filter(RecipeCategory.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return responses.BaseHealthResponse(status_code=fastapi.status.HTTP_204_NO_CONTENT, text="Category deleted")
