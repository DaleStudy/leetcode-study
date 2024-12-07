/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let first = 1;
    let second = 2;

    if (n <= 2) {
        return n;
    }

    for (let i=2; i<n; i++) {
        let tmp = second;
        second = first + second;
        first = tmp;
    }

    return second;
};