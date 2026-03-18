// TC: O(n)
// SC: O(n)
function climbStairs(n: number): number {
    if(n <= 3) {
        return n;
    }
    const memo = new Array(n+1);
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3

    for(let i = 4; i <= n; i++) {
        memo[i] = memo[i-1] + memo[i-2];
    }

    return memo[n];
};
