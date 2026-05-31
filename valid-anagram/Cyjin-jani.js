// tc: O(n)
// sc: 제약조건에 따르면 O(1). 그러나 모든 유니코드 포함될 경우 O(n)
const isAnagram = function (s, t) {
  // 글자수가 다르면 anangram이 성립될 수 없으므로 빠른 return;
  if (s.length !== t.length) return false;

  const data = new Map();

  for (char of s) {
    data.set(char, (data.get(char) || 0) + 1);
  }

  for (let char of t) {
    if (!data.get(char)) return false;
    data.set(char, data.get(char) - 1);
  }

  return true;
};
