import pandas as pd
import os

""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

path = os.getcwd()
# filenames = os.listdir('C:/Users/worac/Desktop/Knowledge/notes/assets')
filenames = os.listdir(path)

df = pd.DataFrame(filenames, columns=['filenames'])
new_path = path + r'\filenames.csv'
print(new_path)
# df.to_csv('C:/Users/worac/Desktop/Knowledge/notes/assets/filenames.csv', index=False)
df.to_csv(new_path, index=False)
