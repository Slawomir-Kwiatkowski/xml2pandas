'''
:description: This program reads data from xml file and creates pandas DataFrame object 
:author: Sławomir Kwiatkowski
:date: 2020-12-19 
'''

import xml.etree.ElementTree as et
from collections import defaultdict
import pandas as pd

persons = defaultdict(list)

tree = et.parse("persons.xml")
root = tree.getroot()
for child in root:
    id = child.attrib.get('id')
    position = child.find('position').text
    first_name = child.find('first_name').text
    last_name = child.find('last_name').text
    email = child.find('email').text
    salary = child.find('salary').text
    
    persons['id'].append(id)
    persons['position'].append(position)
    persons['first_name'].append(first_name)
    persons['last_name'].append(last_name)
    persons['email'].append(email)
    persons['salary'].append(salary)

df = pd.DataFrame(persons, columns=persons.keys()).set_index('id')
df['salary'] = df['salary'].astype(float)
print(df.sort_values(by='salary', ascending=False))