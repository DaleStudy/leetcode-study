/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let preStairs = 0;
    let curStairs = 1;


    for (let i = 0; i < n; i++) {
        let sum = preStairs + curStairs;
        preStairs = curStairs;
        curStairs = sum;
    }

    return curStairs;
};
