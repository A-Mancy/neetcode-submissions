class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == [] or len(nums) == 1:
            return False

        first = nums[0]
        last = nums[len(nums)-1]

        if first == last:
            return True

        for num in nums[1:len(nums)-1]:
            if num == first or num == last:
                return True
                
        return False
        