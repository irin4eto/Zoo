import sqlite3


def create_zoo(cursor):
    cursor.execute('''CREATE TABLE if not exists zoo
                   (name text,
                    capacity int,
                    budget real)''')


def create_zoo_and_animals(cursor):
    cursor.execute('''CREATE TABLE if not exists zoo_and_animals
                   (zoo text,
                    species text,
                    age int,
                    name text,
                    gender text,
                    weight real,
                    status text,
                    FOREIGN KEY (zoo) REFERENCES  zoo(name))''')


def insert_zoo(zoo, cursor):
    cursor.execute("INSERT INTO zoo(name, capacity, budget) VALUES(?, ?, ?)",
                   (zoo.name, zoo.capacity, zoo.budget))


def insert_zoo_and_animals(zoo, animal, cursor):
    cursor.execute("INSERT INTO zoo_and_animals(zoo, species, age, name," +
                   " gender, weight, status) VALUES" +
                   "(?, ?, ?, ?, ?, ?, ?)",
                   (zoo.name, animal.species, animal.age, animal.name,
                    animal.gender, animal.weight, "Alive"))


def create_cursor_and_table(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    create_zoo(cursor)
    create_zoo_and_animals(cursor)
    return cursor


