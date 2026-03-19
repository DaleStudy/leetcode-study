# TC : O(2^target) 재귀 트리의 분기 수
# SC : O(target/min(candidates)) 재귀 스택 깊이

class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        for i in range(len(candidates)):
            self.go(i, candidates, [candidates[i]], candidates[i], target)

        return self.answer

    def go(self, i:int, candidates: List[int], nums: List[int], sum_: int, target: int):
        if sum_ == target:
            self.answer.append(nums.copy())

        for j in range(i, len(candidates)):
            if candidates[j] + sum_ <= target:
                nums.append(candidates[j])
                self.go(j, candidates, nums, sum_ + candidates[j], target)
                nums.pop()

        


            

