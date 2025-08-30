function groupAnagrams(strs: string[]): string[][] {
  const anagramsMap = new Map<string, string[]>();

  for (const word of strs) {
    const anagramKey = [...word].sort().join();

    if (anagramsMap.has(anagramKey)) {
      anagramsMap.get(anagramKey)!.push(word);
    } else {
      anagramsMap.set(anagramKey, [word]);
    }
  }

  return Array.from(anagramsMap.values());
}
