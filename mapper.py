import sqlite3
import random
import datetime


class Mappers:

    def add_violations(self, category, image):
        id = random.randint(1, 100)
        date_time = datetime.datetime.now()
        with sqlite3.connect("traffic_violation.db") as connection:
            cursor = connection.cursor()
            insert_statement = """INSERT INTO violations (id, category, image, timestamp, validated, assigned_to)
                          VALUES (?, ?, ?, ?, ?, ?)"""
            values = (id, category, image, date_time, "No", "Not Assigned")
            cursor.execute(insert_statement, values)
            connection.commit()

    def get_all_violations(self, filter):
        if filter is None:
            with sqlite3.connect("traffic_violation.db") as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM violations"
                cursor.execute(query)
                rows = cursor.fetchall()
        else:
            with sqlite3.connect("traffic_violation.db") as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM violations where category = '" + filter + "'"

                cursor.execute(query)
                rows = cursor.fetchall()
        return rows

    def select_violation(self, id):
        with sqlite3.connect("traffic_violation.db") as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM violations WHERE id = '" + id + "' "
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows

    def validate_violations(self, id):
        with sqlite3.connect("traffic_violation.db") as connection:
            cursor = connection.cursor()
            update_query = (
                """UPDATE violations SET validated = ?, assigned_to = ? WHERE id = ?"""
            )
            values = ("Yes", "MVD", id)
            cursor.execute(update_query, values)
            connection.commit()

    def validate_user(self, username):
        with sqlite3.connect("traffic_violation.db") as connection:
            cursor = connection.cursor()
            query = "SELECT password FROM users WHERE username = '" + username + "' "
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows
