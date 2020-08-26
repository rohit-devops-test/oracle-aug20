
import json  
import pandas as pd  
from pandas.io.json import json_normalize  
  
with open('https://github.com/a9k00r/python-test/blob/master/raw_nyc_phil.json') as f: 
    d = json.load(f) 
  
# lets put the data into a pandas df 
# clicking on raw_nyc_phil.json under "Input Files" 
# tells us parent node is 'programs' 
nycphil = json_normalize(d['programs']) 
nycphil.head(3) 
