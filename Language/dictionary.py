__author__ = 'bst'

myDict = {'key1': 'value1',
          'key2': 'value2'}

for k in myDict.keys():
    print(k)

if 'key1' in myDict:
    print("Found!")

for k,v in myDict.items():
    print(k,v)

for d in myDict:
    print(d)

