/**
 * @param n
 *
 * dp, 슬라이딩 윈도우 사용해서 풀 수 있다.
 *
 * 공간 복잡도를 줄이기 위해서 아래와같이 슬라이딩을 활용할 수 있다.
 *
 * function climbStairs(n: number): number {
 *     if (n <= 2) return n;
 *
 *     let first = 1;  // 1계단을 오르는 방법 수
 *     let second = 2; // 2계단을 오르는 방법 수
 *
 *     for (let i = 3; i <= n; i++) {
 *         let current = first + second;
 *         first = second;
 *         second = current;
 *     }
 *
 *     return second;
 * }
 */


function climbStairs(n: number): number {
    if(n <= 2) return n;

    let dp: number[] = new Array(n+1);
    dp[1] = 1;
    dp[2] = 2;

    for(let i=3;i<=n;i++){
        dp[i] = dp[i-1] +dp[i-2];
    }

    return dp[n]
};
