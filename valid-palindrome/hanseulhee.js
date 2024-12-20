/**
 * @param {string} s
 * @return {boolean}
 *
 * 해결: 먼저 문자열의 정방향, 역방향 비교를 위해 문자열을 소문자로 변환하였으며 특수기호는 제외하였습니다.
 * 정방향과 역방향을 비교하여 문자가 모두 일치하면 true 아니라면 false를 반환하였습니다.
 */
var isPalindrome = function (s) {
  const filterS = s.toLowerCase().replace(/[^a-z0-9]/g, "");

  let left = 0;
  let right = filterS.length - 1;

  while (left < right) {
    if (filterS[left] !== filterS[right]) {
      return false;
    } else {
      left++;
      right--;
    }
  }

  return true;
};
