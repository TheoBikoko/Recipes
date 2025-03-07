from database import read_db, read_db_list

DATA_PATH = "data/products.json"
data= read_db(DATA_PATH, "products")

print(data)

for k,v in data.items():
    print (f"{k}: {v}")

data = read_db_list(DATA_PATH, "products")

print(data)