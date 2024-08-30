from collections import Counter
def most_frequent(s):
    for char, freq in Counter(filter(str.isalpha, s)).most_common():
        print(char, freq)
most_frequent("hello world")
