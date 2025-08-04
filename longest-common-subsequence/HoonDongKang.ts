/**
 * [Problem]: [1143] Longest Common Subsequence
 * (https://leetcode.com/problems/longest-common-subsequence/description/)
 */
function longestCommonSubsequence(text1: string, text2: string): number {
    //시간복잡도 O(2^n)
    //공간복잡도 O(n)
    // Time Limit Exceeded
    function dfsFunc(text1: string, text2: string): number {
        function dfs(i: number, j: number): number {
            if (i === text1.length || j === text2.length) return 0;

            if (text1[i] === text2[j]) {
                return 1 + dfs(i + 1, j + 1);
            } else {
                return Math.max(dfs(i, j + 1), dfs(i + 1, j));
            }
        }

        return dfs(0, 0);
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function memoizationFunc(text1: string, text2: string): number {
        const memo = new Map<string, number>();

        function dfs(i: number, j: number) {
            if (i === text1.length || j === text2.length) return 0;

            const key = `${i}, ${j}`;
            if (memo.has(key)) return memo.get(key)!;

            let result = 0;
            if (text1[i] === text2[j]) {
                result = 1 + dfs(i + 1, j + 1);
            } else {
                result = Math.max(dfs(i, j + 1), dfs(i + 1, j));
            }

            memo.set(key, result);
            return result;
        }

        return dfs(0, 0);
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function dpFunc(tex1: string, text2: string): number {
        const length1 = text1.length;
        const length2 = text2.length;
        const dp: number[][] = Array.from({ length: length1 + 1 }, () =>
            Array(length2 + 1).fill(0)
        );

        for (let i = 1; i <= length1; i++) {
            for (let j = 1; j <= length2; j++) {
                if (text1[i - 1] === text2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[length1][length2];
    }
}
