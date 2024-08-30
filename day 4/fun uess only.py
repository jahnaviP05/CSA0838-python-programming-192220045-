def uses_only(word, letters):
    return all(char in letters for char in word)
print(uses_only("hello", "helo"))  
print(uses_only("world", "helo"))
