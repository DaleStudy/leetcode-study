function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const frequencyMap = {};

  for (const letter of s) {
    if (frequencyMap[letter]) {
      frequencyMap[letter] += 1;
    } else {
      frequencyMap[letter] = 1;
    }
  }

  for (const letter of t) {
    if (frequencyMap[letter]) {
      frequencyMap[letter] -= 1;
    } else {
      return false;
    }
  }

  return true;
}
