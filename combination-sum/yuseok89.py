# TC: O(NlogN)
# SC: O(logN)
class Solution:

    def rec(self, cur, candi, combi, sum, target, ans):

        if sum == target:
            ans.append(combi)

            return

        for idx in range(cur, len(candi)):

            multi = 1

            while sum + multi * candi[idx] <= target:
                self.rec(idx + 1, candi, combi + [candi[idx]] * multi, sum + multi * candi[idx], target, ans)
                multi += 1

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        self.rec(0, candidates, [], 0, target, ans)

        return ans

