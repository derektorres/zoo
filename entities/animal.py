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
        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = """INSERT INTO animales (name, species, age, food) VALUES (%s, %s, %s, %s)"""

            cursor.execute(sql, (name, species, age, food))
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error al guardar el animal:", e)

    def get_all_animals():
        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = """SELECT * FROM animales"""
            cursor.execute(sql)
            rows = cursor.fetchall()

            animals = []
            for row in rows:
                animals.append(Animal(
                    row['id'],
                    row['name'],
                    row['species'],
                    row['age'],
                    row['food']
                ))

            cursor.close()
            connection.close()

            return animals
        except Exception as e:
            print("Error al obtener los animales:", e)
            return []




