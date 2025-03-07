import json

def read_db(data_path, field):
    with open(data_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    items_dict = {item["id"] : item for item in data[field]}
    return items_dict


def save_db(data_path, field, data):
    data = {field: list(data.values())}
    with open(data_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)