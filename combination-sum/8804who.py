class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {}
        
        for i in range(target+1):
            dp[i] = set()

        for candidate in candidates:
            if candidate <= target:
                dp[candidate].add(tuple([candidate]))

        for i in range(target+1):
            for candidate in candidates:
                if i-candidate >= 0:
                    for j in dp[i-candidate]:
                        arr = [nums for nums in j]+[candidate]
                        arr.sort()
                        dp[i].add(tuple(arr))
 
        answer = [list(nums) for nums in dp[target]]
        return answer
    
