//time-complexity : O(n)
//space-complexity : O(1)

const isPalindrome = function (s) {
  let left = 0;
  let right = s.length - 1;
  while (left < right) {
    if (isAlphaNumeric(s[left]) && isAlphaNumeric(s[right])) {
      if (s[left].toLowerCase() === s[right].toLowerCase()) {
        left++;
        right--;
      } else return false;
    } else {
      if (!isAlphaNumeric(s[left])) left++;
      if (!isAlphaNumeric(s[right])) right--;
    }
  }
  return true;
};

const isAlphaNumeric = function (c) {
  return (
    (c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57) ||
    (c.charCodeAt(0) >= 65 && c.charCodeAt(0) <= 90) ||
    (c.charCodeAt(0) >= 97 && c.charCodeAt(0) <= 122)
  );
};
