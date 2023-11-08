import datetime
from typing import Optional

from sqlalchemy import String, Integer, Float, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from features import DbBaseModel


# from features.recipes.categories.models import RecipeCategory
# from features.recipes.instructions.models import RecipeInstruction


class RecipeCategory(DbBaseModel):
    """Recipe category"""
    __tablename__ = "RECIPE_CATEGORIES"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    created_by: Mapped[str] = mapped_column(String(30))
    created_on: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.current_timestamp(), init=False)
    updated_by: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    updated_on: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.current_timestamp(),
                                                          onupdate=func.current_timestamp(), init=False)
    recipes: Mapped[list["Recipe"]] = relationship("Recipe", back_populates="category", init=False)


class Recipe(DbBaseModel):
    """Recipe DB Model"""
    __tablename__ = "RECIPES"

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    picture: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    summary: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    calories: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    carbo: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    fats: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    proteins: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    cholesterol: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    time_to_prepare: Mapped[int] = mapped_column(Integer)
    complexity: Mapped[float] = mapped_column(Float, init=False,nullable=True, default=0)
    created_by: Mapped[str] = mapped_column(String(30))
    created_on: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.current_timestamp(), init=False)
    updated_by: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    updated_on: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.current_timestamp(),
                                                          onupdate=func.current_timestamp(), init=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("RECIPE_CATEGORIES.id"), nullable=True, init=False)
    category: Mapped[RecipeCategory] = relationship("RecipeCategory", back_populates="recipes", init=False)
    instructions: Mapped[list["RecipeInstruction"]] = relationship("RecipeInstruction", back_populates="recipe")


class RecipeInstruction(DbBaseModel):
    """Recipe instruction"""
    __tablename__ = "RECIPE_INSTRUCTIONS"

    id: Mapped[int] = mapped_column(Integer, init=False, autoincrement=True, primary_key=True)
    instruction: Mapped[str] = mapped_column(String(300))
    category: Mapped[str] = mapped_column(String(100))
    time: Mapped[str] = mapped_column(Integer)
    complexity: Mapped[float] = mapped_column(Float)

    recipe_id: Mapped[int] = mapped_column(ForeignKey('RECIPES.id'), nullable=False, init=False)
    recipe: Mapped[Recipe] = relationship('Recipe', back_populates='instructions', init=False)
