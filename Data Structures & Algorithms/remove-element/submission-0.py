class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                      # next position to write a kept value
        for x in nums:
            if x != val:
                nums[k] = x        # move kept values to the front
                k += 1
        return k
