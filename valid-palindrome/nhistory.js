/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 1. Create left and right pointer
  let l = 0;
  let r = s.length - 1;
  // 2. Iterate while loop with l<r condition
  while (l < r) {
    // 3. Check character with left pointer is alphanumeric character or not
    if (
      (s[l] >= "a" && s[l] <= "z") ||
      (s[l] >= "A" && s[l] <= "Z") ||
      (s[l] >= "0" && s[l] <= "9")
    ) {
      // 4. Check character with right pointer is alphanumeric character or not
      if (
        (s[r] >= "a" && s[r] <= "z") ||
        (s[r] >= "A" && s[r] <= "Z") ||
        (s[r] >= "0" && s[r] <= "9")
      ) {
        // 5. Compare left and right pointer character
        if (s[l].toLowerCase() !== s[r].toLowerCase()) {
          return false;
        } else {
          l++;
          r--;
        }
        //    If not, go to next location for right pointer
      } else r--;

      //    If not, go to next location for left pointer
    } else l++;
  }
  return true;
};

// TC: O(n)
// SC: O(n)

console.log(isPalindrome("A man, a plan, a canal: Panama")); //true
console.log(isPalindrome("race a car")); //false
