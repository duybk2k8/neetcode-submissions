class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        res1 = []
        current = 0
        length = 0
        res = set(nums)
        best = 0

        for i in res:
            if i - 1 not in res:
                current = i
                length = 1
            
            while current + 1 in res:
                current += 1
                length += 1
            
            best = max(length, best)

        return best
        