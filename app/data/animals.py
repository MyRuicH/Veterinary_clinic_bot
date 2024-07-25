import json

from app.data import list_files, open_files


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if not animal in animals:
        animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварину '{animal}' успішно записано!"
    else:
        msg = f"Тварина '{animal}' уже записана!"

    return msg


def cure_animal(animal: str) -> str:
    animals = open_files.get_animals()
    cured_animals = open_files.get_cured_animals()

    if animal in animals:
        animals.remove(animal)
        cured_animals.append(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file) 

        with open(list_files.cured_animals, "w", encoding="utf-8") as file:
            json.dump(cured_animals, file) 
        
        msg = f"Тварину '{animal}' успішно вилікувано!"
    else:
        msg = f"Тварина '{animal}' відсутня у списку!"

    return msg


def remove_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        animals.remove(animal)

        with open(list_files.animals, "w", encoding="utf-8") as file:
            json.dump(animals, file)

        msg = f"Тварина '{animal}' успіно видалена!"
    else:
        msg = f"Тварина '{animal}' відсутня у списку!"

    return msg


        