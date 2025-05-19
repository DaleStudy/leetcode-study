/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let maxLength = 0;
    const seen = new Map(); // 문자 -> 마지막 인덱스

    for (let end = 0; end < s.length; end++) {
        const char = s[end];

        // 중복 문자가 이전에 등장했으면 start를 갱신
        if (seen.has(char) && seen.get(char) >= start) {
            start = seen.get(char) + 1;
        }

        seen.set(char, end); // 현재 문자 위치 갱신
        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
};
