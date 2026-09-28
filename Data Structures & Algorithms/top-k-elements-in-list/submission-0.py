from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digit_count = defaultdict(int)
        for num in nums:
            digit_count[num] += 1

        return sorted(digit_count, key=digit_count.get, reverse=True)[:k]

        

        

        