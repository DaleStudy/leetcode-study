class Solution:

    def solve(self, candidates, remsum, cur, res, idx) :
        if remsum == 0 :
            res.append(list(cur))
            return

        if remsum < 0 or idx >= len(candidates) :
            return
        cur.append(candidates[idx])
        self.solve(candidates, remsum-candidates[idx],cur,res,idx)
        cur.pop()
        self.solve(candidates,remsum,cur,res,idx+1)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        self.solve(candidates,target,cur,res,0)
        return res
