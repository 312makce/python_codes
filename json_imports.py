import json
"""
with open('friends_json.txt', 'r') as file:
    file_content = json.load(file) #reads file and trurns into dictionary

print(file_content['friends'][0])
"""
car = [
    {"make": "Ford", "model": "focus"},
    {"make": "Mazda", "model": "6"},
    {"make": "honda", "model": "accord"}
]

with open('friends_json.txt', 'w') as write_file:
    json.dump(car, write_file)

# it is just an example for converting CVS to JSON
json_list = []      # store the converted json data for each line
csv_file = open('csv_file.txt', 'r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)     # write json data to a file
json_file.close()