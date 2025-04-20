/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const result = [];

    const dfs = (start, path, sum) => {
        if (sum === target) {
            result.push([...path]); // 정답 조합 발견
            return;
        }

        if (sum > target) return; // target 초과 -> 백트랙

        for (let i = start; i < candidates.length; i++) {
            path.push(candidates[i]);        // 숫자 선택
            dfs(i, path, sum + candidates[i]); // 같은 인덱스부터 다시 탐색 (중복 사용 허용)
            path.pop();                      // 백트래킹
        }
    };

    dfs(0, [], 0);
    return result;
};
