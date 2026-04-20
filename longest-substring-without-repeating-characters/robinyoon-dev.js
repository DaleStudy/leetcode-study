/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {

    let maxLength = 0;
    let startIndex = 0;
    let endIndex = 0;

    let charSet = new Set();

    // 슬라이딩 윈도우
    while (endIndex < s.length) {
        let currentChar = s[endIndex];
        if (charSet.has(currentChar)) {
            charSet.delete(s[startIndex]);
            startIndex++;
        } else {
            charSet.add(currentChar);
            maxLength = Math.max(maxLength, charSet.size);
            endIndex++;
        }
    }
    return maxLength;
};



