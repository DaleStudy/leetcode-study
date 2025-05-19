/**
 * 문제 설명
 * - 중복되지 않는 가장 긴 부분 문자열의 길이 구하기
 *
 * 아이디어
 * 1) Brute Force - O(n^2)
 * 2) Sliding Window + Hash Set - O(n)
 *   - 투 포인터를 활용하여 시작점과, 끝을 가르키는 두개의 포인터를 사용.
 *   - 끝 포인터가 이미 존재하는 문자열에 포함하는 경우 시작 포인터를 끝 포인터가 존재하지 않는 곳까지 이동시킨다.
 *
 */
function lengthOfLongestSubstring(s: string): number {
  const seen = new Set<string>();
  let left = 0;
  let maxLength = 0;

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }

  return maxLength;
}
