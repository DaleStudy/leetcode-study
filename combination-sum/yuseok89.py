# TC: O(N^T)
# SC: O(T)
class Solution:

    def rec(self, cur_idx, target, candi, cur_combi, ans):

        if target == 0:
            ans.append(cur_combi.copy())

        if cur_idx == len(candi):
            return

        for idx in range(cur_idx, len(candi)):
            if target < candi[idx]:
                continue

            cur_combi.append(candi[idx])
            self.rec(idx, target - candi[idx], candi, cur_combi, ans)
            cur_combi.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        self.rec(0, target, candidates, [], ans)

        return ans

