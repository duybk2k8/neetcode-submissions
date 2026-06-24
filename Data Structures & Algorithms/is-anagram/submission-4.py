class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
             s_dict[i] += 1
        for j in t:
           t_dict[j] += 1
        if s_dict == t_dict:
            return True
        return False
        