"""
    시간 복잡도와 공간복잡도 추후 작성하겠습니다ㅠ
    풀이 보고 하루 뒤에 기억해서 해보려고 했는데도 한참 걸렸네요
"""
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        comb = []
        def recur(n : int):
            if sum(comb) > target :
                return
            elif sum(comb) == target :
                return ans.append(comb.copy())
            else :
                for i in range(n, len(candidates)) :
                    comb.append(candidates[i])
                    recur(i)
                    comb.pop()
        recur(0)
        return ans
