class Solution:
    #idea chính: ["apple", "banana", "cat "] ==> ghép thành string len(x) + "#" + string 
    #decode => xem len # ==> tách

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word))
            s += "#"
            s += word
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        num = ""
        while i < len(s):
            while s[i].isdigit():
                num += s[i]
                i += 1
            length = int(num)
            res.append(s[i + 1 : i + 1 + length])
            i += length + 1
            num = ""
        return res
