/**
 * 문제: https://leetcode.com/problems/climbing-stairs/description/
 *
 * 요구사항:
 * n개의 계단이 있을 때
 * 계단은 1, 2 칸씩 오를 수 있다.
 * 이 계단을 오르는 방법은 총 몇가지 인가?
 *
 * * */

const climbingStairs = (n) => {
    if(n <= 1) return 1;
    let prev1 = 1;
    let prev2 = 1;
    for(let i = 1; i < n; i++) {
        let current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
}
