/**
 *
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let start = 0;
  let maxLength = 0;
  let maxCharCount = 0;
  let count = {};

  for (let end = 0; end < s.length; end++) {
    const char = s[end];
    count[char] = (count[char] || 0) + 1;

    // 현재 윈도우 안에서 가장 많이 나온 문자 수 갱신
    maxCharCount = Math.max(maxCharCount, count[char]);

    // 바꿔야 하는 문자 수가 k보다 많으면 → 왼쪽 포인터 이동
    if (end - start + 1 - maxCharCount > k) {
      count[s[start]]--;
      start++;
    }

    // 현재 윈도우 길이로 최대 길이 갱신
    maxLength = Math.max(maxLength, end - start + 1);
  }

  return maxLength;
};
