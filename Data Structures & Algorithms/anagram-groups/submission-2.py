from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #for each key added to anagram => để default value to list=> tương tự int str
        result = [] #tạo array cho từng kết quả
        #go through each word => check xem có ana k => add vào anagram_map
        #array kết quả, add hết value vào

        for s in strs:
            #sort vào (ví dụ ate eat tea ===> aet ==> đặt làm key + đưa các giá trị original vào key)
            sorted_s = tuple(sorted(s)) 
            #sorted sẽ trả về list ==> ['a', 'e', 't'] => mutable => k làm key dc
            #==> chuyển thành tuple (immutable)
            anagram_map[sorted_s].append(s)
            #bước 1: anagram_map[sorted_s], ví dụ sorted_s là "aet" 
            #=> nó check, k thấy value => defaultdict => tự tạo thành "aet": []
            #bước 2: append trực tiếp s (giả sử là eat) vào hộp value của "aet" ==> "aet": ["eat"]
            #nếu lặp lại, kiểu như "tea" => nó sẽ lại sort thành aet => check xem dict đã có sẵn chưa => truy vấn và add "tea" vào
        for value in anagram_map.values():
            result.append(value)
        return result
            
