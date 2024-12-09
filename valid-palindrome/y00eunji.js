/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const filtered = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
    const reversed = filtered.split('').reverse().join('');

    return filtered === reversed;
};
