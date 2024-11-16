import mysql.connector
from .userQueries import user_queries
from .User import User

class UserRepository:
	def __init__(self) -> None:
		self.mysql_client = mysql.connector.connect(
			host="localhost",
			user="root",
			password="rootroot",
			database="datos_usuarios"
		)
	def getUsers(self):
		cursor = self.mysql_client.cursor(dictionary=True)
		cursor.execute(user_queries["get_users"])
		users = cursor.fetchall()
		cursor.close()
		return users
	def createUser(self, user: User):
		cursor = self.mysql_client.cursor()
		cursor.execute(user_queries["create_user"], user.email, user.name, user.surname, user.password, user.phone, user.age)

	def delete_user(self, user_id: int):
		cursor = self.mysql_client.cursor()
		cursor.execute(user_queries["delete_user"], user_id)
		self.mysql_client.commit()
		return 200

	def update_user(self, user_id: int, user_update: User):
		cursor = self.mysql_client.cursor()
		cursor.execute(user_queries["update_user"], user_update.email, user_update.name, user_update.surname, user_update.password, user_update.phone, user_update.age, user_id)