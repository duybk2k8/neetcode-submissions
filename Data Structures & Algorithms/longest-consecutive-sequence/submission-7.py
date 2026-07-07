class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        best = 0

        for i in res:
            if i - 1 not in res:
                length = 0
            
                while i + length in res:
                    length += 1
            
                best = max(length, best)

        return best
        