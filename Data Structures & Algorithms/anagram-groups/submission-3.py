from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        anagram = defaultdict(list)
        for str in strs:
            n = tuple(sorted(str))
            anagram[n].append(str)
        for i in anagram.values():
            answer.append(i)
        return answer
        