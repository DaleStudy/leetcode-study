/**
 * 문제 설명
 * - 주어진 문자열에서 가장긴 palindromic substring을 찾는 문제
 *
 * 아이디어
 * 1) palindrom을 찾는 법(중심 확장법) + 홀수ver, 짝수ver 두 가지 경우를 모두 확인
 *  - two pointer 기법을 이용하여 확장하면서 가장 긴 palindromic substring을 찾는다.
 */
function longestPalindrome(s: string): string {
  let maxLength = 0;
  let start = 0;

  const expand = (l: number, r: number) => {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      const currentLength = r - l + 1;
      if (currentLength > maxLength) {
        maxLength = currentLength;
        start = l;
      }
      l--;
      r++;
    }
  };

  for (let i = 0; i < s.length; i++) {
    expand(i, i);
    expand(i, i + 1);
  }

  return s.slice(start, start + maxLength);
}
