/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const charCountMap = {};

    for (let char of s) {
        charCountMap[char] = (charCountMap[char] || 0) + 1;
    }

    for (let char of t) {
        if (!charCountMap[char]) {
            return false;
        }

        charCountMap[char] -= 1;
    }

    return true;
};
