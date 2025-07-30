//특정 지점까지 얼마나 많은 개수의 길이 존재할까
//갈 수 있는 방법은 1 혹은 2칸씩 오를 수 있다. 

/* 1. dp로 풀기. 
점화식은 이렇다. 
dp[n] = d[n-1] + d[n-2]
*/

var climbStairs = function(n) {
    if (n === 1) return 1;
    if (n === 2) return 2;

    const dp = Array(n + 1).fill(0);
    dp[1] = 1;
    dp[2] = 2;

    for (let i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
};

//시간복잡도: O(n)
//공간복잡도: O(n)

//2. 메모리 아끼기
//dp배열 없이 변수로만 작성하기
var climbStairs = function(n) {
    if (n === 1) return 1;
    let a = 1, b = 2;
    for (let i = 3; i <= n; i++) {
        let temp = a + b;
        a = b;
        b = temp;
    }
    return b;
};


//시간복잡도: O(n)
//공간복잡도: O(1)