def evenFilter(d):
    return [value for key, value in d.items() if key % 2 == 0]
example_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(evenFilter(example_dict))  
