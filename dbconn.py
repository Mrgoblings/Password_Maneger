import mysql.connector
import datetime
from settings import password_table, users_table
import datetime

FORMAT = "%d-%m-%Y"
near_days = 3


class DataBase:
    def __init__(self, server_name, username, password, dbname):
        # needed for the connection with the db
        self.server_name = server_name
        self.username = username
        self.password = password
        self.database_name = dbname

        # just declaring them in the constructor
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = mysql.connector.connect(host=f"{self.server_name}", user=f"{self.username}", passwd=f"{self.password}",
                                          database=f"{self.database_name}")
        self.cursor = self.db.cursor()

    def disconnect(self):
        self.cursor.close()
        self.db.close()

    def get_id_by_mail(self, user_mail):
        self.connect()
        self.cursor.execute(
            f"SELECT p.User_id from {password_table} p, {users_table} u WHERE u.User_mail = %s AND p.User_id = u.User_id", (user_mail, ))
        user_id = self.cursor.fetchall()[0][0]
        self.disconnect()
        return user_id

    def get_all_passwords_for_user(self, user_mail):
        self.connect()

        self.cursor.execute(f"SELECT p.Sait, p.Login_name, p.Password from {password_table} p, {users_table} u WHERE p.User_id = u.User_id AND u.User_mail = %s", (user_mail,))
        result = self.cursor.fetchall()
        self.disconnect()

        result_json = []

        for elem in result:
            result_json.append({'sait': elem[0], 'login_name': elem[1], 'password': elem[2]})

        return result_json

    def delete_password(self, user_mail, sait, login_name):
        user_id = self.get_id_by_mail(user_mail)

        self.connect()

        self.cursor.execute(f"DELETE FROM {password_table} p WHERE p.User_id = %s AND p.sait = %s AND p.Login_name = %s", (user_id, sait, login_name))
        self.db.commit()

        self.disconnect()
        return

    def insert_password(self, user_mail, sait, login_name, password):
        user_id = self.get_id_by_mail(user_mail)

        self.connect()
        # print()
        self.cursor.execute(
            f"INSERT INTO `{password_table}` (User_id, Password, Login_name, Sait) VALUES (%s, %s, %s, %s)", (user_id, password, login_name, sait))
        self.db.commit()

        self.disconnect()

        return 201

    def edit_password(self, user_mail, sait, login_name, password, which_attribute, updated_attribute):
        user_id = self.get_id_by_mail(user_mail)
        all_attributes = {"sait": "Sait", "login_name": "Login_name", "password": "Password"}

        if which_attribute not in all_attributes:
            return 400

        self.connect()
        # print()
        self.cursor.execute(
            f"UPDATE `{password_table}` SET {all_attributes[which_attribute]} = %s WHERE (User_id, Password, Login_name, Sait) = (%s, %s, %s, %s)", (updated_attribute, user_id, password, login_name, sait))
        self.db.commit()

        self.disconnect()

        return 200


if __name__ == "__main__":
    db = DataBase("localhost", "root", "", "passwordManager")

    # print(db.delete_password("lol", "gogle.som", "maaate123"))
    print(db.edit_password("lol", "goggggle.som", "maaate123", "acsacasca", "lolyloly"))
    print(db.get_all_passwords_for_user("lol"))
