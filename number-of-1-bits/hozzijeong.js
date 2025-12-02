/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    const binary = n.toString(2);


    return binary.replaceAll('0','').length
};
