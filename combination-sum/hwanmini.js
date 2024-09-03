// 시간복잡도: O(c^t)
// 공간복잡도: O(t)

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const result = [];

    const dfs = (startIdx, subset = [], sum = 0) => {
        if (sum > target) return;
        if (sum === target) {
            result.push([...subset]);
            return;
        }


        for (let i = startIdx; i < candidates.length; i++) {
            subset.push(candidates[i]);
            dfs(i, subset, sum + candidates[i]);
            subset.pop();
        }
    };

    dfs(0);

    return result;
};

console.log(combinationSum([2, 3, 6, 7], 7));
