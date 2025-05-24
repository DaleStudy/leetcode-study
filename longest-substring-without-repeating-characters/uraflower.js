/**
 * 문자열에서 중복 문자 없는 가장 긴 부분 문자열의 길이를 반환하는 함수
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = function(s) {
    let start = 0;
    let end = 0;

    const set = new Set();
    let maxSize = 0;

    while (end < s.length) {
        while (set.has(s[end])) {
            set.delete(s[start]);
            start++;
        }

        set.add(s[end]);
        maxSize = Math.max(maxSize, set.size);
        end++;
    }

    return maxSize;
};

// 시간복잡도: O(n) (최대 end로 n번, start로 n번 이동하므로 2n만큼 소요)
// 공간복잡도: O(n)
