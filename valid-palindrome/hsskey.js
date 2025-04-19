/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const cleanStr = s.toLowerCase().replace(/[^a-z0-9]/g, '')
    const reversedStr = [...cleanStr].reverse().join('')

    return cleanStr === reversedStr
};
