from collections import Counter

def first_unique_char(s: str) -> int:
    return next((i for i, char in enumerate(s) if Counter(s)[char] == 1), -1)
s = "loveleetcode"
print("Index of first unique character:", first_unique_char(s))  
