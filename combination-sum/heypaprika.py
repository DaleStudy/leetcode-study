# 어렵네요ㅜ 보고 풀었습니다

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def func(cur_remain, arr, idx):
            if cur_remain == 0:
                ans.append(list(arr))
                return
            elif cur_remain < 0:
                return

            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                func(cur_remain - candidates[i], arr, i)
                arr.pop()

        func(target, [], 0)
        return ans

