'''
Time complexity : O(n ^ (target / min_val))
Space complexity : O(target / min_val)
backtracking 
c = [2], total = 2
c = [2, 2], total = 4
c = [2, 2, 2] total = 6
c = [2, 2, 2, 2] total = 8, 초과 backtrack
c = [2, 2, 2, 3] total = 9, 초과 backtrack
c = [2, 2, 2, 6] total = 12, 초과 backtrack
c = [2, 2, 2, 7] total = 13, 초과 backtrack
c = [2, 2, 3] total = 7 정답 추가
c = [2, 2, 6] total = 10, 초과 backtrack
c = [2, 2, 7] total = 11, 초과 backtrack
....
[2,2,3], [7]

'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()
        backtrack(0, [], 0)
        return result
