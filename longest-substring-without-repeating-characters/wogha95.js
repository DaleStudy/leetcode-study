/**
 * TC: O(S)
 * right의 S만큼 순회 + left의 S만큼 순회
 * (각 순회의 곱이 아닌 합인 이유는 right 순회 동안 left의 최대 순회가 S이기 때문입니다.)
 *
 * SC: O(S)
 * usedCharacter에 S만큼 들어갈 수 있습니다.
 *
 * S: s.length
 */

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  // 1. 사용된 문자를 기록하기 위한 set
  const usedCharacter = new Set();

  // 2. 정답 제출을 위한 부분문자열 최대 길이
  let maxLength = 0;

  // 3. 순회를 위한 포인터 + 각 index에서 최대 문자열길이를 구하기 위한 변수
  let left = 0;
  let right = 0;

  while (left <= right && right < s.length) {
    // 4. [right] 문자가 사용되었으면
    if (usedCharacter.has(s[right])) {
      // 5. 사용된 문자를 발견하기 전까지 left 이동 (+ 사용된 [left] 문자 기록 제거)
      while (s[left] !== s[right]) {
        usedCharacter.delete(s[left]);
        left += 1;
      }

      // 6. [right] 문자와 [left] 문자가 동일하므로 left만 이동
      left += 1;
    } else {
      // 7. [right] 문자가 미사용되었으면 기록 추가
      usedCharacter.add(s[right]);
    }

    // 8. 중복없는 부분문자열 최대 길이 갱신
    maxLength = Math.max(maxLength, right - left + 1);

    // 9. 다음 문자로 이동
    right += 1;
  }

  return maxLength;
};
