/**
 * 중복 문자 없이 가장 긴 부분 문자열의 길이를 찾기 (부분 문자열은 연속된 문자들의 집합이어야 함)
 *
 * 슬라이딩 윈도우(Sliding Window) 기법
 * 접근 방법:
 * 1. 시작포인터(left)와 끝포인터(right)를 사용하여 윈도우 정의
 * 2. 문자의 등장여부는 Map을 사용하여 추적
 * 3. 끝 포인터를 이동시키면서 윈도우 확장
 * 4. 중복 문자가 발견되면 시작 포인터를 이동시켜 윈도우 축소
 * 5. 최대 길이를 업데이트
 *
 * 시간복잡도: O(n), 공간복잡도: O(min(n, m)) (n: 문자열 길이, m: 문자 집합 크기)
 */
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (!s.length) return 0;

  let maxLength = 0;
  let left = 0; // 시작 포인터(윈도우 왼쪽 경계)
  const charMap = new Map();

  for (let right = 0; right < s.length; right++) {
    const currentChar = s[right]; // 현재 문자

    // 현재문자가 이미 Map에 있고, 그 인덱스(위치)가 현재 윈도우 내에 있다면
    if (charMap.has(currentChar) && charMap.get(currentChar) >= left) {
      // 시작포인터(윈도우 왼쪽 경계)를 중복된 문자의 다음위치로 이동
      left = charMap.get(currentChar) + 1;
    }

    // 현재 문자의 인덱스를 Map에 저장
    charMap.set(currentChar, right);

    // 현재 윈도우의 길이와 기존 최대 길이 중 큰 값을 선택
    // right - left + 1: 현재 윈도우의 길이
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength; // 최대 길이 리턴
};
