import csv

with open('data.csv','r') as f:
  data = csv.reader(f)
  print('DATA TYPE: ', type(data))
  print(data)
  for row in data:
        print(row)


reader = csv.DictReader(open("data.csv"))
for raw in reader:
    print(dict(raw))
