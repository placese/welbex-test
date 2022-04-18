import requests
from random import randint, randrange
import names

for _ in range(25):
    r = requests.post("http://localhost:8000/entities", json={"date": "2000-03-18", "title": names.get_first_name(), "quantity": randint(0, 200), "distance": randrange(0, 200)})
    print(r.status_code)
