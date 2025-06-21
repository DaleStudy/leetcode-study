/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let left = 0;
    let maxCount = 0;
    const freq = new Array(26).fill(0); // 알파벳 빈도수 저장
    
    let result = 0;

    for (let right = 0; right < s.length; right++) {
        const idx = s.charCodeAt(right) - 65; // A ~ Z -> 0 ~ 25
        freq[idx]++;
        maxCount = Math.max(maxCount, freq[idx]);

        // 현재 윈도우 크기 - 가장 많은 문자 수 > k 면 왼쪽 포인터 이동
        while ((right - left + 1) - maxCount > k) {
            freq[s.charCodeAt(left) - 65]--;
            left++;
        }

        result = Math.max(result, right - left + 1);
    }

    return result;
};
