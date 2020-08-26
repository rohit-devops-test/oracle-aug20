import pandas as pd 
  
data = pd.read_json('http://api.population.io/1.0/population/India/today-and-tomorrow/?format = json') 
print(data) 
