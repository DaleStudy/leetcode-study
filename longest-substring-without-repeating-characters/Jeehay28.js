/**
 * @param {string} s
 * @return {number}
 */

// 🌟 sliding window technique

// Time Complexity: O(n)
// Why it's O(n)
// - The end pointer iterates over the string exactly once (O(n)).
// - The start pointer also only moves forward without re-processing elements (O(n)).
// - Therefore, the total amount of work done is proportional to the length of the string (n).
// - So, even though there is a while loop inside the for loop, the total work done (number of operations) is still linear, O(n), because the start and end pointers together move across the string just once.
// - This is the key reason why the time complexity is O(n), even with nested loops.

// Space Complexity: O(k), where k k is the length of the longest substring without repeating characters.
// In the worst case, k = n, so O(n)

var lengthOfLongestSubstring = function (s) {
  let start = 0;
  let longest = 0;
  let subString = new Set();

  for (let end = 0; end < s.length; end++) {
    while (subString.has(s[end])) {
      // Shrink the window by moving start
      subString.delete(s[start]);
      start += 1;
    }

    subString.add(s[end]);
    longest = Math.max(longest, end - start + 1);
  }

  return longest;
};

// 🛠️ Solution 1
// Time Complexity: O(n^2), where n is the length of the string s
// Space Complexity: O(k), where k is the length of the longest substring without repeating characters (k ≤ n)

// why the space complexity is not just O(n):
// - Saying O(n) is technically correct in the worst case,
// - but it hides the fact that the actual space usage is proportional to the length of the longest substring without repeats,
// - which could be much smaller than n in many practical cases (e.g., for a string like "aaabbbccc").

// var lengthOfLongestSubstring = function (s) {
//   let longest = 0;

//   for (let i = 0; i < s.length; i++) {
//     let subString = new Set();

//     for (let j = i; j < s.length; j++) {
//       if (subString.has(s[j])) {
//         break;
//       } else {
//         subString.add(s[j]);
//         longest = Math.max(longest, j - i + 1);
//       }
//     }
//   }
//   return longest;
// };

