/**
 *@link https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * 접근 방법 :
 *  - 슬라우딩 윈도우와 set 사용해서 중복없는 문자열 확인
 *  - 중복 문자 발견하면 윈도우 축소
 *
 * 시간복잡도 : O(n)
 *  - 각 문자 순회하니까
 *
 * 공간복잡도 : O(n)
 *  - 중복 없는 경우 최대 n개의 문자 set에 저장
 */
function lengthOfLongestSubstring(s: string): number {
  let start = 0,
    end = 0,
    maxLength = 0;
  const set = new Set<string>();

  while (end < s.length) {
    const char = s[end];

    // 중복이 있으면 윈도우 축소
    if (set.has(char)) {
      set.delete(s[start]);
      start++;
    } else {
      // 중복 없으면 set에 문자 추가, 윈도우 확장
      set.add(char);
      maxLength = Math.max(maxLength, end - start + 1);
      end++;
    }
  }

  return maxLength;
}
