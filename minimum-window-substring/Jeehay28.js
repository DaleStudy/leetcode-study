/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */

// 🚀 sliding window + two pointer approach

// 🕒 Time Complexity: O(n), where n is the length of s
// The inner while loop shrinks the window from the left side but never exceeds the total number of characters in s

// 🗂 Space Complexity: O(m) (or worst case O(n)), where n is the length of t

var minWindow = function (s, t) {
  // early return for the critical edge case
  if (s.length < t.length) {
    return "";
  }

  let windowCnt = new Map();
  let charCnt = new Map();
  let minStart = 0;
  let minEnd = s.length; // set this to an out-of-bounds value initially

  let formed = 0;
  let left = 0;

  // initialize charCount
  // 🔢 t = "ABC", charCount = { A: 1, B: 1, C: 1 }
  for (const ch of t) {
    charCnt.set(ch, (charCnt.get(ch) || 0) + 1);
  }

  // expand the windowCnt
  for (let right = 0; right < s.length; right++) {
    const char = s[right];

    windowCnt.set(char, (windowCnt.get(char) || 0) + 1);

    if (charCnt.has(char) && charCnt.get(char) === windowCnt.get(char)) {
      formed += 1;
    }

    // shrink the window by moving the left pointer
    while (formed === charCnt.size) {
      if (right - left < minEnd - minStart) {
        minStart = left;
        minEnd = right;
      }

      const char = s[left];
      windowCnt.set(char, windowCnt.get(char) - 1);

      if (charCnt.has(char) && windowCnt.get(char) < charCnt.get(char)) {
        formed -= 1;
      }
      left += 1;
    }
  }

  return minEnd === s.length ? "" : s.slice(minStart, minEnd + 1);
};

