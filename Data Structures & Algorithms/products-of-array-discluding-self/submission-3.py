class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = [1]
        right = [1]
        for i in range(1, len(nums)):
            left.append(left[i - 1] * nums[i - 1])
            right.append(right[i - 1] * nums[-i])
        for j in range(len(nums)):
            res.append(left[j] * right[-j - 1])
        return res
