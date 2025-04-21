/**
 * 시간복잡도: O(n)
 *  - 첫번째 for문 O(n)
 *  - 두번째 for문 최대 O(n)
 * 공간복잡도: O(n)
 *  - count O(n)
 */

const isAnagram = (s, t) => {
  if (s.length !== t.length) return false;

  const count = {};

  for (let i = 0; i < s.length; i += 1) {
    count[s[i]] = (count[s[i]] || 0) + 1;
    count[t[i]] = (count[t[i]] || 0) - 1;
  }

  for (const i of Object.values(count)) {
    if (i !== 0) return false;
  }

  return true;
};
