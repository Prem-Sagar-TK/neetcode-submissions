class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen=[]
        occur=[]
        nums = sorted(nums)
        for i in nums:
            if i not in seen:
                seen.append(i)
        for i in seen:
            occur.append(nums.count(i))
        idx=occur.index(max(occur))
        return seen[idx]