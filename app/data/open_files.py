import os
import json

from app.data import list_files


if not os.path.exists(list_files.animals):
    with open(list_files.animals, "w", encoding="utf-8") as fh:
            json.dump([], fh)


if not os.path.exists(list_files.cured_animals):
     with open(list_files.cured_animals, "w", encoding="utf-8") as file:
          json.dump([], file)


def get_animals(path: str = list_files.animals) -> list:
    with open(path, "r", encoding="utf-8") as fh:
     animals = json.load(fh)

     return animals
    

def get_cured_animals(path: str = list_files.cured_animals) -> list:
     with open(path, "r", encoding="utf-8") as file:
          cured_animals = json.load(file)

     return cured_animals