def group_anagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
words = ["eat", "tin", "ate", "nit", "bat"]
print(group_anagrams(words))
