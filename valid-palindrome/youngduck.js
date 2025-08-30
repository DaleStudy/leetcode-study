/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 1. toLowerCase() - O(n)
  // 2. replace(/[^a-z0-9]/g, '') - O(n)
  const clean = s.toLowerCase().replace(/[^a-z0-9]/g, '');

  // 3. [...clean] 스프레드 연산자 - O(n)
  // 4. reverse() - O(n)
  // 5. join('') - O(n)
  const reverse = [...clean].reverse().join('');

  // 6. 문자열 비교 - O(n)
  return clean === reverse;
};

// 시간복잡도 O(n)
// 공간복잡도 O(n)
