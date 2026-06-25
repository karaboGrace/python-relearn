class Solution:
    def twoSum(self, nums, target) :
        """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
        num_to_index = {} 
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_index:
                return [num_to_index[compliment], index]
            num_to_index[num] = index
sol = Solution()
nums = [1,2,3,4,5]
target = 7
print(sol.twoSum(nums,target))