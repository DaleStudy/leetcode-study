// 시간복잡도: O(log n)
// 공간복잡도: O(log n)

const replaceZeroToEmptyString = (str) => str.replaceAll('0','')


/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    const binaryNum = n.toString(2)
    const replacedNumber = replaceZeroToEmptyString(binaryNum)
    return replacedNumber.length
};


console.log(hammingWeight(11));
console.log(hammingWeight(128));
console.log(hammingWeight(2147483645));
