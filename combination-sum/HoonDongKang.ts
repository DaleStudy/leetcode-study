/**
 * [Problem]: [39] Combination Sum
 *
 * (https://leetcode.com/problems/combination-sum/description/)
 */
function combinationSum(candidates: number[], target: number): number[][] {
    // 시간복잡도: O(c^t)
    // 공간복잡도 O(t)
    function dfsFunc(candidates: number[], target: number): number[][] {
        let result: number[][] = [];
        let nums: number[] = [];

        function dfs(start: number, total: number): void | number[][] {
            if (total > target) return;
            if (total === target) {
                result.push([...nums]);
                return result;
            }
            for (let i = start; i < candidates.length; i++) {
                let num = candidates[i];
                nums.push(num);
                dfs(i, total + num);
                nums.pop();
            }
        }

        dfs(0, 0);
        return result;
    }

    // 시간복잡도: O(c*t)
    // 공간복잡도 O(c*t)
    function dpFunc(candidates: number[], target: number): number[][] {
        const dp: number[][][] = Array(target + 1)
            .fill(null)
            .map(() => []);

        dp[0] = [[]];

        for (const num of candidates) {
            for (let t = num; t <= target; t++) {
                for (const comb of dp[t - num]) {
                    dp[t].push([...comb, num]);
                }
            }
        }

        return dp[target];
    }

    return dpFunc(candidates, target);
}

console.log(combinationSum([2, 3, 6, 7], 7));
