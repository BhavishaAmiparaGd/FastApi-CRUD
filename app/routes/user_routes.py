from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.crud.user_crud import create_user, get_user, update_user, delete_user

router = APIRouter()

@router.post("/users/", response_model=User)
def create_new_user(user: User):
    return create_user(user)

@router.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    db_user = get_user(user_id)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}", response_model=User)
def update_existing_user(user_id: int, updated_user: User):
    updated = update_user(user_id, updated_user)
    if updated:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_existing_user(user_id: int):
    deleted = delete_user(user_id)
    if deleted:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")