/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const filteredLowercaseChars = [...s.toLowerCase()].filter(char => (char.charCodeAt() >= 97 && char.charCodeAt() <= 122) || (char.charCodeAt() >= 48 && char.charCodeAt() <= 57));

    const filteredLowercaseCharsLength = filteredLowercaseChars.length;

    for (let i = 0; i < filteredLowercaseCharsLength / 2; i++) {
        if (filteredLowercaseChars[i] !== filteredLowercaseChars[filteredLowercaseCharsLength - 1 - i]) return false;
    }

    return true;
};

// 시간 복잡도 : O(n)
// 공간 복잡도 : O(n)
