def hasDuplicate(nums):
    seen = set()
    for i in nums:
          if i in seen:  
              return True 
          else: 
              seen.add(i)    
    return False   
nums = [1, 2, 3, 4, 5]
print(hasDuplicate(nums)) 