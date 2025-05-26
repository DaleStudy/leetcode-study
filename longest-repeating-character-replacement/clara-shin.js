/**
 * 최대 k번 문자 변경 후, 가장 긴 동일문자 부분문자열 찾기
 * 문자열 s와 정수 k, 최대 k번까지 문자를 다른 영문대문자로 바꿀 수 있음
 * 동일한 문자로 구성된 가장 긴 부분문자열 길이를 리턴해라
 *
 * 슬라이딩 윈도우 사용(문자열을 한번만 순회)
 * 윈도우 내에서, 가장 많이 등장하는 문자를 제외한 나머지 문자들이, k개 이하일 때만, 유효한 부분 문자열이다
 * 조건을 만족하지 않으면 윈도우의 왼쪽 포인터를 오른쪽으로 이동하여 윈도우 크기를 줄인다
 *
 * 시간복잡도 O(n)
 * 공간복잡도 O(1) - 문자 빈도수 저장배열 크기는 항상 26 고정
 */

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  // 문자 빈도수를 저장할 배열 (A-Z: 65-90) 0으로 초기화
  const charCount = new Array(26).fill(0);

  let left = 0; // 윈도우 왼쪽 끝
  let maxCount = 0; // 현재 윈도우에서 가장 많이 등장하는 문자의 빈도수
  let maxLength = 0; // 결과: 가장 긴 부분 문자열 길이

  // 윈도우의 오른쪽 끝 이동
  for (let right = 0; right < s.length; right++) {
    // 현재 문자의 빈도수 증가 (문자 코드를 인덱스로 변환)
    const charIndex = s.charCodeAt(right) - 65;
    charCount[charIndex]++;

    // 현재 윈도우에서 가장 많이 등장하는 문자의 빈도수 업데이트
    maxCount = Math.max(maxCount, charCount[charIndex]);

    // 현재 윈도우에서 변경해야 할 문자 수가 k를 초과하면 윈도우의 왼쪽을 이동
    // 현재 윈도우에서 변경해야 할 문자 수: 윈도우 크기 - 가장 많이 등장하는 문자의 빈도수
    // 윈도우 크기: right - left + 1
    if (right - left + 1 - maxCount > k) {
      // 왼쪽 문자의 빈도수 감소
      const leftCharIndex = s.charCodeAt(left) - 65;
      charCount[leftCharIndex]--;
      left++;
    }

    // 현재 윈도우 크기로 최대 길이 업데이트
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
};
