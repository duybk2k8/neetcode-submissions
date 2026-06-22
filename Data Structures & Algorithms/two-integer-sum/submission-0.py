class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j and i not in solution and j not in solution:
                    solution.append(i)
                    solution.append(j)
        return solution
