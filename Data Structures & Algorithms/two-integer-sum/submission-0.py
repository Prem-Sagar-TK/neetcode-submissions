class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          # value -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]     # earlier index first
            seen[n] = i
        return []