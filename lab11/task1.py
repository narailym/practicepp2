import psycopg2
import re
def connection():
    return psycopg2.connect(
    host="localhost",
    database = "suppliers",
    user = "postgres",
    password = "acerAN"
    )
def deletebook():
    mode = input("delete: ").strip().lower()
    with connection() as conn:
        with conn.cursor() as cur:
            if mode == "name":
                name = input("name for delete: ")
                cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
            elif mode == "phone":
                phone = input("number for delete")
                cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
            else:
                print("incorrect")
                return
            conn.commit()
            print("Deleted")
deletebook()

def returnall():
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name,number FROM phonebook ORDER BY name;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
returnall()
def insert_update():
    name = input()
    number = input()

    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name, ))
            if cur.fetchone():
                cur.execute("UPDATE contacts SET phone_number = %s WHERE name = %s;", (number, name))
                print("updated")
            else:
                cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s);", (name, number))
                print("new contact")
            conn.commit()

insert_update()
def error_num(number):
    return (re.fullmatch(r'(87\d{9}|\+77\d{9}|7\d{9})', number))
def manyusers3():
    with connection() as conn:
        with conn.cursor() as cur:
            numofuserinsert = int(input())
            errors = []

            for _ in range(numofuserinsert):
                name = input("name: ")
                phone = input("phone number: ")

                if error_num(phone):
                    cur.execute("INSERT INTO contacts (name, phone_number) VALUES (%s, %s)", (name, phone))
                else:
                    errors.append((name, phone))

            conn.commit()

            if errors:
                print("Invalid numbers:")
                for name, phone in errors:
                    print(f"{name}: {phone}")
            else:
                print("A"
                      "all phone numbers are valid")

manyusers3()

def limitcont():
    limit = input()
    offset = input()


    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s;", (limit, offset))
            for row in cur.fetchall():
                print(row)
limitcont()
