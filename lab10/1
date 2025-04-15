import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database = "suppliers",
    user = "postgres",
    password = "acerAN"
)

def create_table():
    command = """
           CREATE TABLE IF NOT EXISTS phonebook (
           id SERIAL PRIMARY KEY,
           name VARCHAR(255),
           category VARCHAR(255),
           number VARCHAR(20)
           )
           """
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()


def insert_values(name, category, number):
    # Проверка на существование данных в таблице
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM phonebook WHERE name = %s AND number = %s", (name, number))
        if not cur.fetchone():  # Если данных нет
            command = "INSERT INTO phonebook(name, category, number) VALUES (%s, %s, %s)"
            cur.execute(command, (name, category, number))
            conn.commit()
        else:
            print(f"Entry with name {name} and number {number} already exists.")




def insert_by_csv(filename):
    command = "INSERT INTO phonebook(name, category, number) VALUES (%s, %s, %s)"
    with conn.cursor() as cur:
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            _ = next(csvreader)
            for row in csvreader:
                name, category, number = row
                cur.execute(command, (name, category, number))
                conn.commit()


def update(column, what, towhat):
    with conn.cursor() as cur:
        command = f"UPDATE phonebook SET {column}=%s WHERE {column}=%s"
        cur.execute(command, (towhat, what))
        conn.commit()


def query_data_by_name(name):
    with conn.cursor() as cur:
        command = f"SELECT * FROM phonebook WHERE name=%s"
        cur.execute(command, (name,))
        return cur.fetchall()


def query_data_by_category(category):
    with conn.cursor() as cur:
        command = f"SELECT * FROM phonebook WHERE category=%s"
        cur.execute(command, (category,))
        return cur.fetchall()


def delete_data(who):
    with conn.cursor() as cur:
        command = "DELETE FROM phonebook WHERE name=%s"
        cur.execute(command, (who,))
        conn.commit()



create_table()
insert_values("arailym", "me", "+7081698640")
insert_values("Timur", "family", "+7736699993")
insert_by_csv("phonebook.csv")
#update("name", "Timur","Amir")
#delete_data("arailym")
conn.close()

