// https://leetcode.com/problems/climbing-stairs/

// 공간 복잡도 개선 후 풀이

// time complexity : O(n)
// space complexity : O(1)
function climbStairs(n: number): number {
    if (n < 3) {
        return n;
    }
    let pre = 1;
    let cur = 2;
    for (let i = 0; i < n - 2; i++) {
        let temp = pre;
        pre = cur;
        cur = temp + pre;
    }
    return cur;
};

// 공간 복잡도 개선 전 풀이

// time complexity : O(n)
// space complexity : O(n)

// function climbStairs(n: number): number {
//     const dp = {1: 1, 2: 2}
//     for (let i = 3; i < n + 1; i++) {
//         dp[i] = dp[i - 1] + dp[i - 2];
//     }
//     return dp[n]
// };
