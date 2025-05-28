/**
 * 문자열 s에서 문자열 t의 모든 문자(중복 포함)를 포함하는 가장 짧은 부분 문자열을 찾는 문제
 * 시간복잡도: O(m + n), 공간복잡도: O(m + n)
 */

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (s.length < t.length) return '';

  // t의 각 문자별 필요한 개수를 Map으로 저장
  const need = new Map();
  for (let char of t) {
    need.set(char, (need.get(char) || 0) + 1);
  }

  let left = 0;
  let right = 0;
  let valid = 0; // 조건을 만족하는 문자 종류 수
  let minLen = Infinity;
  let start = 0;

  // 현재 윈도우의 문자별 개수
  const window = new Map();

  while (right < s.length) {
    // 윈도우에 문자 추가
    const rightChar = s[right];
    right++;

    // 필요한 문자인 경우에만 처리
    if (need.has(rightChar)) {
      window.set(rightChar, (window.get(rightChar) || 0) + 1);
      if (window.get(rightChar) === need.get(rightChar)) {
        valid++;
      }
    }

    // 윈도우 축소 시도
    while (valid === need.size) {
      // 더 작은 윈도우 발견시 업데이트
      if (right - left < minLen) {
        start = left;
        minLen = right - left;
      }

      // left를 이동시키며 윈도우에서 문자 제거
      const leftChar = s[left];
      left++;

      if (need.has(leftChar)) {
        if (window.get(leftChar) === need.get(leftChar)) {
          valid--;
        }
        window.set(leftChar, window.get(leftChar) - 1);
      }
    }
  }

  return minLen === Infinity ? '' : s.substring(start, start + minLen);
};
