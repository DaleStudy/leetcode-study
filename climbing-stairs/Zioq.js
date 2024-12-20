/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    // 1 -> 1
    // 2 -> (1+1) | 2
    // 3 -> (1+1+1) | (1+2) | (2+1)
    // 4 -> (1+1+1+1) | (2+1+1) | (1+2+1) | (1+1+2) | (1+2+2)
    // 5 -> (1+1+1+1+1) | (2+1+1+1) | (1+2+1+1) | (1+1+2+1) | (1+1+1+2) | (1+2+2) | (2+1+2) | (2+2+1)
    if(n <=3) return n

    let a = 0;
    let b = 1;
    let c = 0;

    for(let i=0; i<n; i++) {
        c = a+b;
        a = b;
        b = c;
    }
    return b;
};


console.log(climbStairs(2))
console.log(climbStairs(3))
console.log(climbStairs(4))
console.log(climbStairs(5))