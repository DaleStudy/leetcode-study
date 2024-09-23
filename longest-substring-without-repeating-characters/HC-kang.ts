/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters
 * T.C. O(n^2)
 * S.C. O(n)
 */
// function lengthOfLongestSubstring(s: string): number {
//   let max = 0;
//   for (let i = 0; i < s.length; i++) {
//     const SET = new Set();
//     let count = 0;
//     for (let j = i; j < s.length; j++) {
//       if (SET.has(s[j])) break;
//       SET.add(s[j]);
//       count += 1;
//       max = Math.max(max, count);
//     }
//   }
//   return max;
// }

/**
 * T.C. O(n)
 * S.C. O(n)
 */
// function lengthOfLongestSubstring(s: string): number {
//   let left = 0;
//   let right = 0;
//   let max = 0;
//   const SET = new Set();

//   while (s[right]) {
//     if (SET.has(s[right])) {
//       SET.delete(s[left]);
//       left++;
//     } else {
//       SET.add(s[right]);
//       max = Math.max(SET.size, max);
//       right++;
//     }
//   }

//   return max;
// }

/**
 * T.C. O(n)
 * S.C. O(n)
 */
function lengthOfLongestSubstring(s: string): number {
  let left = 0;
  let right = 0;
  let max = 0;
  const MAP = new Map<string, number>();

  while (right < s.length) {
    if (MAP.has(s[right])) {
      left = Math.max(MAP.get(s[right])! + 1, left);
    }
    MAP.set(s[right], right);
    max = Math.max(max, right - left + 1);
    right++;
  }

  return max;
}
