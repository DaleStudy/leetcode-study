// naive한 풀이
// tc: O(n)
// sc: O(n)
const isPalindromeNaive = function (s) {
  const str = s.toLowerCase().replace(/[^a-z0-9]/g, ''); // 이 부분에서 공간복잡도가 O(n)
  let leftIdx = 0;
  let rightIdx = str.length - 1;

  while (leftIdx <= rightIdx) {
    if (str[leftIdx] !== str[rightIdx]) {
      return false;
    } else {
      leftIdx++;
      rightIdx--;
    }
  }
  return true;
};

// 좀 더 최적화 된 풀이
// tc: O(n)
// cs: O(1)
const isPalindrome = function (s) {
  let leftIdx = 0;
  let rightIdx = s.length - 1;

  while (leftIdx < rightIdx) {
    while (leftIdx < rightIdx && !isAlphaNumeric(s[leftIdx])) leftIdx++;
    while (leftIdx < rightIdx && !isAlphaNumeric(s[rightIdx])) rightIdx--;

    if (s[leftIdx].toLowerCase() !== s[rightIdx].toLowerCase()) return false;

    leftIdx++;
    rightIdx--;
  }
  return true;
};

function isAlphaNumeric(char) {
  return /[a-zA-Z0-9]/.test(char);
}
