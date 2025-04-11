/**
 * [Idea]
 * s에서 각 문자가 몇번 등장하는지 세어준다. (charCount)
 * t에서 문자의 개수를 세어주면서 charCount의 값을 감소시킨다.
 * 문자의 개수가 부족하거나 남는다면 애너그램이 아니다.
 *
 * [Time Complexity]
 * O(n + n + k) => O(n) (n: s와 t의 길이, k: 두 문자열에 등장하는 고유 문자 수)
 *
 * [Space Complexity]
 * O(n)
 * 문자 등장 횟수를 세어주는 charCount에 필요한 공간
 */
function isAnagram(s: string, t: string): boolean {
  const charCount: Record<string, number> = {};
  for (const char of s) {
    charCount[char] = (charCount[char] ?? 0) + 1;
  }

  for (const char of t) {
    if (charCount[char] === undefined || charCount[char] === 0) {
      return false;
    }
    charCount[char]--;
  }

  return Object.values(charCount).every((count) => count === 0);
}
