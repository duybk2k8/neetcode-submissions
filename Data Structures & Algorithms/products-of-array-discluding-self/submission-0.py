class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            value = 1
            nums_alt = nums.copy()
            nums_alt.pop(i)
            for j in nums_alt:
                value *= j
            res.append(value)
        return res
