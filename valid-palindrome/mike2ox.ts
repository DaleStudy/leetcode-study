/**
 * Source: https://leetcode.com/problems/valid-palindrome/
 * 풀이방법: 문자열을 조건에 맞게 정제한 후 reverse하여 비교
 * 시간복잡도: O(n)
 * 공간복잡도: O(n)
 *
 * 생각나는 풀이방법
 * 1. 정규식을 이용하여 문자열을 정제한 후 reverse하여 비교 => 정규식 작성을 못해서 배제
 * 2. 문자열을 순회하면서 조건에 맞는 문자만 배열에 저장한 후 reverse하여 비교
 */
function isPalindrome(s: string): boolean {
  // 미리 길이가 2보다 작은 경우는 true로 반환(Palindrome 조건에 맞음)
  if (s.length < 2) return true;
  const formatted: string[] = [];

  // 문자열을 순회하면서 조건에 맞는 문자만 소문자로 변환해서 배열에 저장
  for (let c of s) {
    if (
      (c >= "a" && c <= "z") ||
      (c >= "A" && c <= "Z") ||
      (c >= "0" && c <= "9")
    )
      formatted.push(c.toLowerCase());
  }
  // formatted 배열을 reverse하여 JSON.stringify로 비교 (중요)
  // ? toReverse()가 chrome console에서는 작동하는데 여기서는 왜 안되는지 모르겠음
  const reversed = [...formatted].reverse();
  return JSON.stringify(reversed) === JSON.stringify(formatted);
}
