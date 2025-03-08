from pathlib import Path

from starlette import status

from database import read_db_list, save_db_list
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DATA_PATH = Path(__file__).parent / Path("data/recipes.json")
recipes_list = read_db_list(DATA_PATH, "recipes")

class RecipeOutput(BaseModel):
    id: int
    name: str
    ingredients: list[str]
    instructions: list[str]
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list[str]
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list[str]

class RecipeInput(BaseModel):
    name: str
    ingredients: list[str]
    instructions: list[str]
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list[str]
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list[str]

@app.get("/")
async def home():
    return {"message": "Welcome to the recipe API. With this API you can create, read, update and delete recipes and also filter them at your convenience."}

@app.get("/recipes", response_model = list[RecipeOutput])
def read_all_recipes() -> list:
    return recipes_list

@app.get("/recipes/{recipe_id}", response_model = RecipeOutput)
def read_specific_recipe(recipe_id: int) -> RecipeOutput:
   for recipe in recipes_list:
       if recipe["id"] == recipe_id:
           return recipe
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found, cannot be read")

@app.post("/recipes", response_model = RecipeOutput)
def create_recipe(new_recipe: RecipeInput):
    new_id = max((recipe["id"] for recipe in recipes_list), default=0) + 1
    new_recipe = new_recipe.dict()
    new_recipe["id"] = new_id
    recipes_list.append(new_recipe)
    save_db_list(DATA_PATH, recipes_list)
    return new_recipe

@app.patch("/recipes/{recipe_id}", response_model = RecipeOutput)
def update_recipe(recipe_id: int, updated_recipe : RecipeInput) -> RecipeOutput:
    updated_recipe = updated_recipe
    for recipe in recipes_list:
       if recipe["id"] == recipe_id:
            recipe.update(updated_recipe)
            save_db_list(DATA_PATH, recipes_list)
            return recipe
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found, it cannot be updated.")

@app.delete("/recipes/{recipe_id}",response_model = RecipeOutput)
def delete_recipe(recipe_id: int) -> RecipeOutput:
    for recipe in recipes_list:
       if recipe["id"] == recipe_id:
           recipes_list.remove(recipe)
           save_db_list(DATA_PATH, recipes_list)
           return recipe
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found, it cannot be deleted.")

