function groupAnagrams(strs: string[]): string[][] {
  const map = new Map();

  for(const str of strs) {
      const key = str.split('').sort().join('');
      const value = map.get(key);
      map.set(key, value ? [...value, str] : [str])
  }
  return Array.from(map.values());
};
