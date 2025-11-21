/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // 피보나치 수열을 활용해서 정답을 풀어야할까?
    // 피보나치 수열이란: F(n) = F(n - 1) + F(n - 2);
    // 반환 조건은 n이 1또는 0일 때 해당 수를 반환할 수 있음
    // 이 문제에서는 2 계단 오르는 상황을 포함시켜야해서 n 이 2일 때 2를 반환하도록 설정
    // 근데 이제 시간초과가 발생해서 캐싱 해줘야함.
    var cache = { '0': 0, '1': 1, '2': 2 };

    var fibo = (n) => {
        let result = 0;
        
        if (typeof(cache[n]) === 'number') {
            result = cache[n];
        } else {
            result = cache[n] = fibo(n - 1) + fibo(n - 2);
        }

        return result;
    };

    return fibo(n);
};
