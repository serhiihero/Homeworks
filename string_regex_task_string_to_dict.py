# there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}
import re

persons = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
persons_ref = re.sub(r's{5}', '', persons)
persons_split = re.split(r'\W', persons_ref)
while "" in persons_split:
    persons_split.remove('')
persons_dict = dict(zip(persons_split[::2], persons_split[1::2]))
print(persons_dict)
