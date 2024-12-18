/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  // 길이가 다르면 false
  if (s.length !== t.length) {
    return false;
  }

  // s 빈도수, t 빈도수
  const countS = {};
  const countT = {};

  // 하나씩 비교하기
  for (let i = 0; i < s.length; i++) {
    countS[s[i]] = (countS[s[i]] || 0) + 1;
    countT[t[i]] = (countT[t[i]] || 0) + 1;
  }

  // 두 객체 동일하면 true, 아니면 false
  for (let char in countS) {
    if (countS[char] !== countT[char]) {
      return false;
    }
  }
  return true;
};

// 시간복잡도: for문 순회 비교하므로 O(n)
// 공간복잡도: countS, countT 최대 n개의 키 가질 수 있으므로 O(n)
