
// 맵 자료 구조를 통해서 각 문자의 개수를 카운트 해서 비교
var isAnagram = function (s, t) {
  const map = new Map();

  for (let i = 0; i < s.length; i++) {
    map.set(s[i], (map.get(s[i]) || 0) + 1);
  }

  for (let i = 0; i < t.length; i++) {
    map.set(t[i], (map.get(t[i]) || 0) - 1);
  }

  return Array.from(map.values()).every((value) => value === 0);
};

console.log(isAnagram("anagram", "nagaram"));
console.log(isAnagram("rat", "car"));
