import sqlite3


def create_zoo(cursor):
    cursor.execute('''CREATE TABLE zoo
                   (name text,
                    capacity int,
                    budget real)''')


def create_zoo_and_animals(cursor):
    cursor.execute('''CREATE TABLE zoo_and_animals
                   (zoo text,
                    species text,
                    age int,
                    name text,
                    gender text,
                    weight real
                    FOREIGN KEY (zoo) REFERENCES  zoo(name))''')

conn_zoo = sqlite3.connect("zoo.db")
cursor_zoo = conn_zoo.cursor()
create_zoo(cursor_zoo)

conn_zoo_and_animals = sqlite3("zoo_and_animals.db")
cursor_zoo_and_animals = conn_zoo_and_animals.cursor()
create_zoo_and_animals(cursor_zoo_and_animals)

