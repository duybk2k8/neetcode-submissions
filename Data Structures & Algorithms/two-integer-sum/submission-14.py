from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_set = defaultdict(int)
        solution=[]


        for i, num in enumerate(nums): #enumerate là lấy cái i cả giá trị
            diff = target - num
            if diff in sum_set:
                return [sum_set[diff], i]
            sum_set[num] = i #3:0
        return
        