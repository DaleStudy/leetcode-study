/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
    let i = "1";

    while (n > 2) {
        n % 2 ? i += "1" : "";
        n = Math.floor(n / 2);
    }

    return i.length;
};

// TC: O(log n)
// SC: O(log n)
