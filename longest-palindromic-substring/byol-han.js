/**
 * https://leetcode.com/problems/longest-palindromic-substring/submissions/1694755721/
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  // 결과로 반환할 가장 긴 팰린드롬 초기값
  let result = '';

  // 팰린드롬의 중심에서 양쪽으로 확장하는 함수
  function expandAroundCenter(left, right) {
    // 왼쪽이 0 이상, 오른쪽이 문자열 길이 이하이며
    // 양쪽 문자가 같으면 계속 확장
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }
    // while문을 빠져나오면 팰린드롬이 아님.
    // 현재 찾은 팰린드롬 반환
    return s.slice(left + 1, right);
  }

  // 문자열의 각 문자를 중심으로 확장 시도
  for (let i = 0; i < s.length; i++) {
    // 홀수 길이 팰린드롬 (중심이 한 글자)
    const oddPalindrome = expandAroundCenter(i, i);
    // 짝수 길이 팰린드롬 (중심이 두 글자)
    const evenPalindrome = expandAroundCenter(i, i + 1);

    // 더 긴 팰린드롬 선택
    if (oddPalindrome.length > result.length) {
      result = oddPalindrome;
    }
    if (evenPalindrome.length > result.length) {
      result = evenPalindrome;
    }
  }

  // 결과 반환
  return result;
};
