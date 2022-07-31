from typing import Collection
from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/user')
async def find_all_users():
    return serializeList(conn.mytestdb.user.find())

# @user.get('/{id}')
# async def find_one_user(id):
#     return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    conn.mytestdb.user.insert_one(dict(user))
    return serializeList(conn.mytestdb.user.find())

@user.put('/{id}')
async def update_user(id,user: User):
    conn.mytestdb.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(conn.mytestdb.user.find_one_and_delete({"_id":ObjectId(id)}))