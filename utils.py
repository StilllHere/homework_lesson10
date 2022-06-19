import json

def load_data():
    """
    получили список словарей из json
    :return:
    """
    with open('candidates.json', encoding="UTF-8") as f:
        l_candidates = json.load(f)

    return l_candidates
#load_data()

