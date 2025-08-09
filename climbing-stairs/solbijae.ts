function climbStairs(n: number): number {
    if (n <= 3) return n;

    // 첫 시도: 시간 복잡도 O(2^n), 공간 복잡도 O(n)
    // return climbStairs(n - 1) + climbStairs(n - 2);

    // 두번째 시도: 시간 복잡도 O(n), 공간 복잡도 O(1)
    let prev1 = 2, prev2 = 1;
    for (let i = 3; i <= n; i++) {
        const curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }

    return prev1;
};
