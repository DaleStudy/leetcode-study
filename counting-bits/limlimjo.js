// 시간복잡도: O(n log n)
// 공간복잡도: O(n)

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    let result = [];
    for (let i=0; i<=n; i++) {
        result.push(i.toString(2).replace(/0/g, '').length);
    }

    return result;
};
