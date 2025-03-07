import json

# dictionaries

def read_db(data_path, field):
    with open(data_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    items_dict = {item["id"]: item for item in data[field]}
    return items_dict


def save_db(data_path, data):
    data = {"products": list(data.values())}
    with open(data_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# lists

def read_db_list(data_path, field):
    with open(data_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data[field]


def save_db_list(data_path, data):
    data = {"products": data}
    with open(data_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
