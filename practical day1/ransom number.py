from collections import Counter

def can_construct(ransomNote: str, magazine: str) -> bool:
    return not Counter(ransomNote) - Counter(magazine)
ransomNote = "aa"
magazine = "aab"
print("Can construct ransom note:", can_construct(ransomNote, magazine))  
