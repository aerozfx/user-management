user_queries = {
    "get_users": "SELECT * FROM usuarios", 
	"create_user": "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s, %s)",
	"delete_user": "DELETE FROM usuarios WHERE id=%s",
	"update_user": "UPDATE usuarios SET email = %s, name = %s, surname = %s, password = %s, phone = %s, age = %s WHERE id = %s"
}