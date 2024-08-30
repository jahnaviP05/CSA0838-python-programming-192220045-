from collections import defaultdict
def print_anagram_sets(words):
    anagram_dict = defaultdict(list)
    for word in words:
        anagram_dict[''.join(sorted(word))].append(word)
    for group in anagram_dict.values():
        if len(group) > 1:
            print(group)
words = input("Enter a list of words separated by spaces: ").split()
print_anagram_sets(words)
