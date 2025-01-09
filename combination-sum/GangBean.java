class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        /**
        1. understanding
        - find all combinations, which sum to target
        - can use same number multiple times
        2. strategy
        - dp[target]: all combination, which sum to target
        - dp[n + 1] = dp[n] | dp[1]
        - [2,3,6,7], target = 7
            - dp[0] = [[]]
            - dp[1] = [[]]
            - dp[2] = [[2]]
            - dp[3] = [[3]]
            - dp[4] = dp[2] | dp[2] = [[2,2]]
            - dp[5] = dp[2] | dp[3] = [[2,3]]
            - dp[6] = dp[2] | dp[4] , dp[3] | dp[3] = [[2,2,2], [3,3]]
            - dp[7] = dp[2] | dp[5], dp[3] | dp[4], dp[6] | dp[1], dp[7] = [[2,2,3],]
        3. complexity
        - time: O(target * N) where N is length of candidates
        - space: O(target * N)
        */
        List<List<Integer>>[] dp = new List[target + 1];
        for (int i = 0; i <= target; i++) {
            dp[i] = new ArrayList<>();
        }

        dp[0].add(new ArrayList<>());

        for (int candidate : candidates) {
            for (int i = candidate; i <= target; i++) {
                for (List<Integer> combination : dp[i - candidate]) {
                    List<Integer> newCombination = new ArrayList<>(combination);
                    newCombination.add(candidate);
                    dp[i].add(newCombination);
                }
            }
        }

        return dp[target];
    }
}

