class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_count= sorted(counts, key=counts.get, reverse=True)
        return sorted_count[:k]
        