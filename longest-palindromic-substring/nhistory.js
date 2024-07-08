var longestPalindrome = function (s) {
  let maxStart = 0,
    maxEnd = 0;

  for (let i = 0; i < s.length; i++) {
    let start = i,
      end = i;
    while (start >= 0 && end < s.length && s[start] === s[end]) {
      if (end - start > maxEnd - maxStart) {
        maxStart = start;
        maxEnd = end;
      }
      start--;
      end++;
    }

    (start = i), (end = i + 1);
    while (start >= 0 && end < s.length && s[start] === s[end]) {
      if (end - start > maxEnd - maxStart) {
        maxStart = start;
        maxEnd = end;
      }
      start--;
      end++;
    }
  }

  return s.slice(maxStart, maxEnd + 1);
};

// TC: O(n^2)
// SC: O(1)
