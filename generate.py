from api.request import Request
from api.review import Review
from random import random
from loader import Loader

filename = "populate.sql"

start = int(input('start id: '))
count = int(input('count: '))

with open(filename, 'w') as file:
    loader = Loader("generating script...", "done!", 0.05).start()
    for i in range(start, 2*(start+count), 2):
        query = None
        if random() > .5:
            request = Request(i, i, i+1)
            query = request.insert()
        else:
            review = Review(i, i, i+1)
            query = review.insert()
        
        file.write(query+"\n")
    loader.stop()

print(f"script written at ./{filename}")