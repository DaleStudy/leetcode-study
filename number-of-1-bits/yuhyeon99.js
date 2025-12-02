/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    var answer = 0;
    while(n >= 1) {
        if (n % 2 === 1) answer ++;
        n = Math.floor(n/2);
    }
    return answer;
};
