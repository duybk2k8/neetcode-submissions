class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        res1 = []
        cnt = 1
        nums1 = sorted(nums)
        res = sorted(set(nums1))

        for j in range(len(res) - 1):
            if res[j + 1] == res[j] + 1:
                cnt += 1
            else:
                res1.append(cnt)
                cnt = 1
        res1.append(cnt)
        if nums == []:
            return 0
        else:
            return max(res1)
        