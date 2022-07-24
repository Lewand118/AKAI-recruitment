import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        file = open('./taski.json', mode='w', encoding='utf-8')
        file.write(json.dumps(tasks))
        file.close()
