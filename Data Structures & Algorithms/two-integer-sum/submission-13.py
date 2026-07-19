class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_with_index = {}
        for i in range(len(nums)):
            num_with_index[nums[i]] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_with_index:
                j = num_with_index[diff]
                if i != j:
                    return [i, j]
        return []
            
