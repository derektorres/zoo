from persistence.db import get_connection


class Animal:
    def __init__(self, id:int, name:str, species:str, age:int, food:str):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.food = food

    @staticmethod
    def save(name, species, age, food):
        connection = get_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = """INSERT INTO animales (name, species, age, food) VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (name, species, age, food))
                nuevo_id = cursor.lastrowid
                connection.commit()
                return nuevo_id
            except Exception:
                connection.rollback()
                raise
            finally:
                cursor.close()
        finally:
            connection.close()

    @staticmethod
    def get_all_animals():
        connection = get_connection()
        try:
            cursor = connection.cursor()
            try:
                sql = """SELECT * FROM animales"""
                cursor.execute(sql)
                rows = cursor.fetchall()

                animals = []
                for row in rows:
                    animals.append(Animal(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4]
                    ))

                return animals
            finally:
                cursor.close()
        finally:
            connection.close()
