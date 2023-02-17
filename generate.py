from api.request import Request

print("-- requests --")
start = int(input('start: '))
count = int(input('count: '))

with open('populate.sql', 'w') as file:
    for i in range(start, 2*(start+count-1), 2):
        request = Request(i, i, i+1)
        file.write(request.insert())

print("done.")