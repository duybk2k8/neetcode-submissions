from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans = []
        for i in nums:
            freq[i] += 1
        
        return [num for num, count in sorted(
            freq.items(), 
            key=lambda x: x[1], 
            reverse=True)[:(k)]]
