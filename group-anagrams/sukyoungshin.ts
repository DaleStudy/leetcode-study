// 1. 객체사용
function groupAnagrams1(strs: string[]): string[][] {
  let anagramGroups: Record<string, string[]> = {};
  for (const word of strs) {
    const sortedKey = [...word].sort().join("");

    if (sortedKey in anagramGroups) {
      anagramGroups[sortedKey].push(word);
    } else {
      anagramGroups[sortedKey] = [word];
    }
  }

  return Object.values(anagramGroups);
};

// 2. Map 사용
function groupAnagrams2(strs: string[]): string[][] {
  let anagramGroups = new Map<string, string[]>();
  for (const word of strs) {
    const key = [...word].sort().join("");

    if (anagramGroups.has(key)) {
      anagramGroups.get(key)?.push(word);
    } else {
      anagramGroups.set(key, [word]);
    }
  }

  return [...anagramGroups.values()];
};
