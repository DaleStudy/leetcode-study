/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const memo = {};

    function dfs(x, y) {
        if (x >= m || y >= n) return 0;
        if (x === m - 1 && y === n - 1) return 1;

        const key = `${x},${y}`;
        if (key in memo) return memo[key];

        memo[key] = dfs(x + 1, y) + dfs(x, y + 1);
        return memo[key];
    }

    return dfs(0, 0);
};
