function groupAnagrams(strs: string[]): string[][] {
  const hashMap = new Map();
  for (let i = 0; i < strs.length; i++) {
    const key = Array.from(strs[i]).sort().join("");

    if (!hashMap.has(key)) {
      hashMap.set(key, [strs[i]]);
    } else {
      hashMap.get(key).push(strs[i]);
    }
  }
  return Array.from(hashMap.values());
}
