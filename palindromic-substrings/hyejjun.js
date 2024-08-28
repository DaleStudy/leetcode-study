/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function (s) {
    let count = 0;

    function checkPalindromic(left, right) {
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            count++;
            left--;
            right++;
        }

    }

    for (let i = 0; i < s.length; i++) {
        checkPalindromic(i, i);
        checkPalindromic(i, i + 1);
    }

    return count;
};

console.log(countSubstrings("abc"));
console.log(countSubstrings("aaa"));


/*
Time Complexity : O(n^2)
Space Complexity: O(1)
*/
