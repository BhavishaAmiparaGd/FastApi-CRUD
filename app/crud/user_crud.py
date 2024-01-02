from app.database.database import database
from app.models.user import User

def create_user(user: User):
    query = "INSERT INTO userdata (name, email, password) VALUES (%s, %s, %s)"
    values = (user.name, user.email, user.password)
    database.cursor.execute(query, values)
    database.connection.commit()
    return {**user.dict(), "id": database.cursor.lastrowid}

def get_user(user_id: int):
    query = "SELECT * FROM userdata WHERE id = %s"
    database.cursor.execute(query, (user_id,))
    return database.cursor.fetchone()

def update_user(user_id: int, updated_user: User):
    query = "UPDATE userdata SET name=%s, email=%s, password=%s WHERE id=%s"
    values = (updated_user.name, updated_user.email, updated_user.password, user_id)
    database.cursor.execute(query, values)
    database.connection.commit()
    return {"message": "User updated successfully"}

def delete_user(user_id: int):
    query = "DELETE FROM userdata WHERE id = %s"
    database.cursor.execute(query, (user_id,))
    database.connection.commit()
    return {"message": "User deleted successfully"}
