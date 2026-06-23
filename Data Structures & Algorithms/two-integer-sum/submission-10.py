from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_set = defaultdict(int)
        solution=[]


        for i, num in enumerate(nums): #enumerate là lấy cái i cả giá trị
            if (target - nums[i]) in sum_set:
                solution.append(i)
                solution.append(sum_set[target - nums[i]])
            sum_set[num] = i #3:0
        solution.sort()
        return solution
        