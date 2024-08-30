def find_unique_words(list1, list2):
    return list(set(list1) - set(list2))
list1 = ['apple', 'banana', 'cherry', 'date']
list2 = ['banana', 'date', 'fig']

print(find_unique_words(list1, list2))
