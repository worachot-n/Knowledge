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
# print('path', path)
# print(*filenames, sep="\n")

for filename in filenames:
    old_name = filename
    new_name = filename.replace(" ", "-")
    # new_name = filename.replace("--", "-")
    # new_name = filename.replace("_", "-")
    os.rename(old_name, new_name)
    # os.rename(filename, filename.replace(" ", "-"))
    # print(filename)
print(*filenames, sep="\n")
