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



# ----

# TC : O(n^(T/M))
# SC : O(T/M)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []
        
        def go(sub_answer: List[int], idx: int, sub_sum: int):
            
            if sub_sum == target:
                answer.append(sub_answer.copy())
                return
            
            for i in range(idx, len(candidates)):
                
                if sub_sum + candidates[i] <= target:
                    sub_answer.append(candidates[i])
                    go(sub_answer, i, sub_sum + candidates[i])
                    sub_answer.pop()
        
        go([], 0, 0)

        return answer

