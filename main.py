from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from model import User

app = FastAPI()

from database import (
    create_user,
    login_user,
    change_user,
    fetch_one_pokemon
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"Hello": "FastAPI"}



@app.get("/api/route/get/{username}", response_model=User)
async def get_pokemon_by_username(username):
    response = await fetch_one_pokemon(username)
    if response:
        return response
    raise HTTPException(404, f"there is no user with this username {user}")



@app.post("/api/route/save", response_model=User)
async def signup(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")



@app.post("/api/route/login/{username}", response_model=User)
async def get_user_by_id(username):
    response = await login_user(username)
    if response:
        return response
    raise HTTPException(404, f"there is no user with this name {user}")



@app.put("/api/update-user/{username}", response_model=User)
async def update_todo(user: User):
    result = await change_user(user.username, user.pokemon)
    if not result: raise HTTPException(400)
    return result
