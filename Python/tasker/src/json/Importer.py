import json


class Importer:

    def __init__(self):
        self.data = None

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        file = open('./taski.json', mode='r', encoding='utf-8')
        self.data = json.load(file)
        file.close()

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.data