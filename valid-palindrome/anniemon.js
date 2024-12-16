/**
 * 시간 복잡도:
 * s.length만큼 탐색. 즉, O(n)
 * 공간 복잡도:
 * 변수와 함수만 저장. 즉, O(1)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  const isAlphaNumeric = (v) => {
      return (/^[a-z0-9]$/i).test(v);
  };

  let l = 0;
  let r = s.length - 1;
  while(l < r) {
      while(!isAlphaNumeric(s[l]) && l < r) {
          l++;
      }
      while(!isAlphaNumeric(s[r]) && l < r) {
          r--;
      }

      if(s[l].toLowerCase() !== s[r].toLowerCase()) {
          return false;
      }
      l++;
      r--;
  }
  return true;
};
