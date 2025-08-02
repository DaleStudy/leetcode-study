/**
 * @param {number} n
 * @return {number}
 * 점화식: f(n) = f(n-1) + f(n-2)
 * 초기값: f(1) = 1, f(2) = 2
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */

var climbStairs = function(n) {
    // 초기값 처리
    if (n === 1) return 1;
    if (n === 2) return 2;

    let prev = 1;
    let curr = 2;

    // 점화식 계산
    for (let i = 3; i <= n; i++) {
        const next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
};
