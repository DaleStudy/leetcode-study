function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const list: Record<string, number> = {};
  for (const key of s) {
    list[key] = (list[key] ?? 0) + 1;
  }

  for (const key of t) {
    if (key in list) {
      list[key] -= 1;
    }
  }

  for (const value in list) {
    if (list[value] > 0) {
      return false;
    }
  }

  return true;
}

isAnagram("anagram", "nagaram"); // true
isAnagram("rat", "car"); // false
isAnagram("a", "ab"); // false
