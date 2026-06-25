def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_word = ''.join(sorted(s))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        anagrams[sorted_word].append(s)
    return list(anagrams.values())