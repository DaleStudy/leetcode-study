/**
 * @description
 * brainstorming:
 * 1. brute force -> time limited
 * 2. recursion -> failed to implement
 * 3. dynamic programming -> failed to implement
 * 4. dale solution https://www.algodale.com/problems/longest-repeating-character-replacement/
 * n: length of list1 + list2
 * time complexity: O(n^3)
 * space complexity: O(n)
 */

/**
 * brute force
 * time complexity: O(n^3)
 * space complexity: O(n)
 */
// var characterReplacement = function (s, k) {
//   let answer = 0;
//   const set = new Set();
//   for (let i = 0; i < s.length; i++) set.add(s[i]);
//   for (let i = 0; i < s.length; i++) {
//     for (const now of set) {
//       let current = 0;
//       let count = k;

//       for (let j = i; j < s.length; j++) {
//         if (now === s[j]) current++;
//         else if (count) {
//           current++;
//           count--;
//         }
//         break;
//       }
//       answer = Math.max(answer, current);
//     }
//   }

//   return answer;
// };

/**
 * time complexity: O(n)
 * space complexity: O(1)
 */
var characterReplacement = function (s, k) {
  let start = 0;
  let answer = 0;

  const map = new Map();
  for (let i = 0; i < s.length; i++) map.set(s[i], 0);

  for (let end = 0; end < s.length; end++) {
    map.set(s[end], map.get(s[end]) + 1);
    const maxLength = Math.max(...map.values());

    while (end - start + 1 - maxLength > k) {
      map.set(s[start], map.get(s[start]) - 1);
      start++;
    }

    answer = Math.max(end - start + 1, answer);
  }

  return answer;
};
