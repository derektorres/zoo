import pytest
from entities.animal import Animal

def test_save_animal():
    name = "Test Animal"
    species = "Test Species"
    age = 5
    food = "Test Food"

    animal_id = Animal.save(name, species, age, food)

    assert animal_id is not None