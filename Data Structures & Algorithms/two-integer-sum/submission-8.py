class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_set = set()
        solution=[]
        for n in nums:
            sum_set.add(n)
        for i in range(len(nums)):
            if (target - nums[i]) in sum_set and i != nums.index(target - nums[i]) and i not in solution:
                solution.append(i)
                solution.append(nums.index(target - nums[i]))
    
        solution.sort()
        return solution 