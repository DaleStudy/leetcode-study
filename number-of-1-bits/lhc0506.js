/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    return [...(n).toString(2)].reduce((acc, cur) => cur === '1' ? acc + 1 : acc, 0);
};

//시간 복잡도 : O(logn)
//공간 복잡도 : O(logn)
