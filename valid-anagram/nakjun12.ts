function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  // 공간 복잡도: O(k)
  const hash: { [key: string]: number } = {};

  // 시간 복잡도: O(n)
  for (let char of s) {
    hash[char] = (hash[char] || 0) + 1;
  }

  // 시간 복잡도: O(n)
  for (let char of t) {
    if (!hash[char]) return false;
    hash[char]--;
  }

  return true;
}
