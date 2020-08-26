import json

person_dict = {"name": "Raj",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.json', 'w') as json_file:
  json.dump(person_dict, json_file)
