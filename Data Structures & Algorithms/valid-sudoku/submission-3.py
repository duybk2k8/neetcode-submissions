from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = 0
        res1 = 0
        res2 = 0
        #Check hàng
        for i in range(9):
            cnt = defaultdict(int)
            for j in range(9):
                cnt[board[i][j]] += 1
            for key, value in cnt.items():
                if key != "." and value > 1:
                    res += 1

        #Check cột
        for i in range(9):
            cnt1 = defaultdict(int)
            for j in range(9):
                cnt1[board[j][i]] += 1
            for key, value in cnt1.items():
                if key != "." and value > 1:
                    res1 += 1    
        
        #Check 3x3
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                cnt2 = defaultdict(int)
                for m in range(i, i + 3, 1):
                    for n in range(j, j + 3, 1):
                        cnt2[board[m][n]] += 1
                for key, value in cnt2.items():
                    if key != "." and value > 1:
                        res2 += 1

        if res1 == 0 and res2 == 0 and res == 0:
            return True
        else:
            return False
