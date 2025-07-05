/**
 * [Problem]: [338] Counting Bits
 * (https://leetcode.com/problems/counting-bits/description/)
 */
function countBits(n: number): number[] {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function dpFunc(n: number): number[] {
        const dp = new Array(n + 1).fill(0);
        let offset = 1;

        for (let i = 1; i <= n; i++) {
            if (offset * 2 === i) {
                offset = i;
            }

            dp[i] = 1 + dp[i - offset];
        }

        return dp;
    }

    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function optimizedFunc(n: number): number[] {
        const dp = new Array(n + 1).fill(0);
        for (let i = 0; i <= n; i++) {
            dp[i] = dp[i >> 1] + (i & 1);
        }
        return dp;
    }
}
