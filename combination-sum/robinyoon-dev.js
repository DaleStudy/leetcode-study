/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {

    const result = [];

    function dfs(remainTarget, currentArray, currentIndex) {

        if (remainTarget < 0) {
            return;
        }

        if (remainTarget == 0) {
            result.push([...currentArray]);
            return;
        }

        // 백트래킹 탐색
        for (let i = currentIndex; i < candidates.length; i++) {
            currentArray.push(candidates[i]);

            dfs(remainTarget - candidates[i], currentArray, i);

            currentArray.pop();
        }

    }

    dfs(target, [], 0);

    return result;

};
