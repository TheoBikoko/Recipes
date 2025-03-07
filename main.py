from pathlib import Path
from database import read_db, save_db, read_db_list
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



DATA_PATH = Path(__file__).parent / Path("data/recipes.json")
DATA = read_db_list(DATA_PATH, "recipes")


class Recipe(BaseModel):
    id: int
    name: str
    ingredients: list
    instructions: list
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list

class RecipeOutput(BaseModel):
    id: int
    name: str
    ingredients: list
    instructions: list
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list

class RecipeInput(BaseModel):
    name: str
    ingredients: list
    instructions: list
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list
    userId: int
    image: str
    rating: float
    reviewCount: int
    mealType: list

@app.get("/")
async def home():
    return {"message": "Welcome to the recipe manager. With this program you can create, read, update and delete recipes and also filter them at your convenience."}

@app.get("/recipes", response_model = list(RecipeOutput))
def read_all() -> list:
    return DATA

@app.get("/recipes/recipe_id", response_model = RecipeOutput)
def read(recipe_id: int):
    if recipe_id not in DATA:
        raise KeyError("Recipe not found")
    return DATA[recipe_id]

#@app.post("/recipes")


#@app.put("/recipes/{recipe_id}")


#@app.delete("/recipes/{recipe_id}")