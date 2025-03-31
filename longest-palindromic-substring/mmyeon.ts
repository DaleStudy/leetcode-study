/**
 *
 * 접근 방법 :
 *  - 팰린드롬은 좌우 대칭 문자열을 찾아야 한다.
 *  - 문자열 중심이 1개(홀수)일 때와 2개(짝수)일 때 고려해서 팰린드롬을 확장하며 긴 문자열을 리턴한다.
 *
 * 시간복잡도 : O(n^2)
 *  - n = s 문자열 길이
 *  - 동일 문자인 경우 for문과 while문에서 2번 순회 발생 O(n)
 *
 * 공간복잡도 : O(1)
 *  - 고정된 변수만 사용
 *
 */
function longestPalindrome(s: string): string {
  let result = "";

  function expandFromCenter(start: number, end: number) {
    while (start >= 0 && end < s.length && s[start] === s[end]) {
      start--;
      end++;
    }
    return s.slice(start + 1, end);
  }

  for (let i = 0; i < s.length; i++) {
    const oddPalindrome = expandFromCenter(i, i);
    if (oddPalindrome.length > result.length) result = oddPalindrome;

    const evenPalindrome = expandFromCenter(i, i + 1);
    if (evenPalindrome.length > result.length) result = evenPalindrome;
  }

  return result;
}
