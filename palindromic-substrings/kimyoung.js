var countSubstrings = function (s) {
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    let left = i,
      right = i; // odd length substrings
    helper(s, left, right);

    (left = i), (right = i + 1); // even length substrings
    helper(s, left, right);
  }
  function helper(s, l, r) {
    // increment result and keep expanding left and right, while left and right indexes are within range and they're equal
    while (l >= 0 && r <= s.length && s[l] === s[r]) {
      result++;
      l--;
      r++;
    }
  }
  return result;
};

// test cases
console.log(countSubstrings("abc")); // 3
console.log(countSubstrings("aaa")); // 6
console.log(countSubstrings("a")); // 1
console.log(countSubstrings("")); // 0

// space - O(1) - constant variable `result`
// time - O(n^2) - iterating through the string and expanding both ways