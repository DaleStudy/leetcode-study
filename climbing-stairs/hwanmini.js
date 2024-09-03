// 시간복잡도 O(n)
// 공간복잡도 O(n)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const stairs = [1, 2]

    for (let i = 2; i < n; i++) {
        stairs[i] = stairs[i-1] + stairs[i-2]
    }

    return stairs[n-1]
};

console.log(climbStairs(5))
