/**
 * [Problem]: [62] Unique Paths
 * (https://leetcode.com/problems/unique-paths/description/)
 */

function uniquePaths(m: number, n: number): number {
    //시간복잡도 O(2^(m*n))
    //공간복잡도 O(m*n)
    // Time Limit Exceeded
    function dfsFunc(m: number, n: number): number {
        let result: number = 0;
        function dfs(row: number, col: number) {
            if (row === m - 1 && col === n - 1) result++;
            if (row + 1 < m) dfs(row + 1, col);
            if (col + 1 < n) dfs(row, col + 1);
        }

        dfs(0, 0);
        return result;
    }

    //시간복잡도 O(m*n)
    //공간복잡도 O(m*n)
    function memoizationFunc(m: number, n: number): number {
        let memo = new Map<string, number>();

        function dfs(row: number, col: number) {
            const key = `${row}|${col}`;

            if (memo.has(key)) return memo.get(key);
            if (row === m - 1 && col === n - 1) return 1;
            if (row >= m || col >= n) return 0;

            const result = dfs(row + 1, col) + dfs(row, col + 1);

            memo.set(key, result);
            return result;
        }

        return dfs(0, 0);
    }
    //시간복잡도 O(m*n)
    //공간복잡도 O(m*n)
    function dpFunc(m: number, n: number): number {
        let dp: number[][] = Array.from({ length: m }, () => Array(n).fill(1));

        for (let i = 1; i < m; i++) {
            for (let j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];
    }
    //시간복잡도 O(m*n)
    //공간복잡도 O(n)
    function optimizationFunc(m: number, n: number): number {
        let dp: number[] = new Array(n).fill(1);
        for (let i = 1; i < m; i++) {
            let left = 1;
            for (let j = 1; j < n; j++) {
                dp[j] += left;
                left = dp[j];
            }
        }

        return dp[n - 1];
    }
}
