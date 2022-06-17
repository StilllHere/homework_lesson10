import json

def load_data():
    """
    получили список словарей из json
    :return:
    """
    with open('candidates.json', encoding="UTF-8") as f:
        templates = json.load(f)

    return templates
#load_data()

