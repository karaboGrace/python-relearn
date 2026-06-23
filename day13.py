s = input("Enter the first string: ")
t = input("Enter the second string: ")
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    count = {}
    counts = {}
    for char in s:  
        count[char] = count.get(char, 0) + 1
    for c in t:
        counts[c] = counts.get(c, 0) + 1
    return count == counts
print(isAnagram(s,t))
"""
Alternatively, you can use the Counter class from the collections module to simplify the code:
from collections import Counter

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
"""