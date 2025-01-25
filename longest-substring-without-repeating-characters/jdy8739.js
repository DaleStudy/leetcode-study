/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let end = 0;

    const set = new Set();

    let max = 0;

    while (end < s.length) {
        const char = s[end];

        if (set.has(char)) {
            set.delete(s[start]);

            start++;
        } else {
            set.add(char);

            end++;
        }

        max = Math.max(max, set.size);
    }

    return max;
};

// 시간복잡도 O(2n) -> 최대 2n번 반복
// 공간복잡도 O(n) -> 최대 s의 길이만큼 공간을 사용
