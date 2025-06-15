/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (s.length < t.length) return "";

    // 1. t의 문자 개수를 세기
    const targetMap = new Map();
    for (let char of t) {
        targetMap.set(char, (targetMap.get(char) || 0) + 1);
    }

    let left = 0;
    let right = 0;
    let minLen = Infinity;
    let minStart = 0;

    let required = targetMap.size; // 만족시켜야 할 문자 종류 수
    let formed = 0;
    const windowMap = new Map();

    while (right < s.length) {
        const char = s[right];
        windowMap.set(char, (windowMap.get(char) || 0) + 1);

        // 문자 개수가 딱 맞는 경우
        if (targetMap.has(char) && windowMap.get(char) === targetMap.get(char)) {
            formed++;
        }

        // 모든 문자가 충족될 경우 -> 왼쪽 포인터 당겨보기
        while (left <= right && formed === required) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            const leftChar = s[left];
            windowMap.set(leftChar, windowMap.get(leftChar) - 1);
            if (targetMap.has(leftChar) && windowMap.get(leftChar) < targetMap.get(leftChar)) {
                formed--;
            }
            left++;
        }

        right++;
    }

    return minLen === Infinity ? "" : s.slice(minStart, minStart + minLen);
};
