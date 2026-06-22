// 피보나치 수열 문제
const climbStairs = (n) => {
// f(n) = f(n-1) + f(n-2)
    if (n <= 2) return n;

    let prev2 = 1;
    let prev1 = 2;

    for (let i = 3; i <= n; i++) {
        let current = prev1 + prev2; 
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
};
