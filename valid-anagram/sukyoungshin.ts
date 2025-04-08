// 1번풀이 (hashTable)
function isAnagram1(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const charCount: Record<string, number> = {};

  for (const char of s) {
    charCount[char] = (charCount[char] ?? 0) + 1;
  }

  for (const char of t) {
    if (!charCount[char]) return false;
    charCount[char]--;
  }

  return true;
};

// 2번풀이 (sort)
function isAnagram2(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const sortedS = s.split('').sort().join('');
  const sortedT = t.split('').sort().join('');

  return sortedS === sortedT;
};

