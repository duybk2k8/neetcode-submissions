from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_map = defaultdict(int)
        result = 0
        
        for n in nums:
            dup_map[n] += 1
        
        for value in dup_map.values():
            if value > 1:
                result += 1

        if result != 0:
            return True
        else:
            return False
        