from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            #tạo mảng 26 phần tử, đại diện 26 chữ cái a-z
            #ý tưởng: key là số lần suất hiện từng chữ cái
            #vdu: "tea" => "a" "e" "t" = [1,0,0,0,1,0...,0,1]
            for c in s:
                count[ord(c) - ord("a")] += 1
            #ord là lấy giá trị ascii: vdu: a=80 b=81 ==> map a 0 => 80-80 map b 1 => 81 - 80
            res[tuple(count)].append(s) #count is list => mutable => tuple
        return list(res.values())