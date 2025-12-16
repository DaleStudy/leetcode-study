class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combination(index, cur_comb, cur_sum):
            if cur_sum == target:
                ans.append(cur_comb[:])
                return
            if cur_sum > target or index >= len(candidates):
                return
            cur_comb.append(candidates[index])
            combination(index, cur_comb, cur_sum + candidates[index])
            # 합이 target이랑 같던지, 크던지, 길이를 넘던지하면 return으로 탈출
            # 그 외에 다른 경우의 수를 봐야하므로 
            # 마지막꺼는 다시 빼고 어쨌든 index 넘겨서 다시 combination 확인해봐야함
            cur_comb.pop()
            combination(index + 1, cur_comb, cur_sum)
            return ans
            
        return combination(0, [], 0)
