var isPalindrome = function (s) {
  // remove any special characters and space from the string
  const formattedString = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
  // use split() method to separate each charaters and put them in an array - reverse it - concatenate
  const reversedString = formattedString.split('').reverse().join('');

  return reversedString === formattedString;
};

// time complexity: O(n)
// space complexity: O(n)
