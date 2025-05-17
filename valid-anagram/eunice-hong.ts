function isAnagram(s: string, t: string): boolean {
  // if the length of the two strings are not the same, return false
  if (s.length !== t.length) return false;

  // create a map of the characters in string s and t
  const sMap = new Map();
  const tMap = new Map();

  // iterate through the strings and add the characters to the maps
  for (let i = 0; i < s.length; i++) {
    sMap.set(s[i], (sMap.get(s[i]) ?? 0) + 1);
    tMap.set(t[i], (tMap.get(t[i]) ?? 0) + 1);
  }

  // if the values of the maps are not the same, return false
  for (let char of sMap.keys()) {
    if (sMap.get(char) !== tMap.get(char)) {
      return false;
    }
  }
  return true;
}
