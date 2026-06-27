def topKFrequent(nums, k):
    dic = {}    
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    return sorted(dic.keys(), key=lambda x: dic[x], reverse=True)[:k]
