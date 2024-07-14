var countSubstrings = function (s) {
  let count = 0;

  const isPalindrom = (start, end) => {
    while (start >= 0 && end < s.length && s[start] === s[end]) {
      start--;
      end++;
      count++;
    }
  };

  for (let i = 0; i < s.length; i++) {
    isPalindrom(i, i); // odd number of str
    isPalindrom(i, i + 1); // even number of str
  }
  return count;
};

// TC: O(n^2)
// SC: O(1)
