/**
 * 주어진 문자열에서 최대 k개를 대체해 가장 긴 동일 문자 반복 부분 문자열을 만들 수 있을 때,
 * 이 문자열의 길이를 반환하는 함수
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 const characterReplacement = function(s, k) {
    let start = 0;
    let end = 0;
    let counter = {};
    let maxFrequent = 0; // 현재 구간에 가장 많이 포함되어 있는 알파벳의 총 개수
    let maxLength = 0;

    while (start <= end && end < s.length) {
        counter[s[end]] = (counter[s[end]] || 0) + 1;
        maxFrequent = Math.max(maxFrequent, counter[s[end]]);

        while (end - start + 1 - maxFrequent > k) {
            counter[s[start]]--;
            start++;
        }

        maxLength = Math.max(end - start + 1, maxLength);
        end++;
    }

    return maxLength;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
