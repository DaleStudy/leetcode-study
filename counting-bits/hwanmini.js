// 시간복잡도 O(n * log n)
// 공간복잡도 O(n)

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    const result = []

    for (let i = 0 ; i <= n; i++) {
        const binaryNumber = i.toString(2)
        const oneLength = binaryNumber.replaceAll('0','').length

        result.push(oneLength)
    }

    return result
};

console.log(countBits(5))
