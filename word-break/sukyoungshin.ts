function wordBreak(s: string, wordDict: string[]): boolean {
  const cache: Record<string, boolean> = {};

  function canSplit(str: string): boolean {
    if (str === "") return true;
    if (cache[str] !== undefined) return cache[str];

    for (let i = 1; i <= str.length; i++) {
      const left = str.slice(0, i);
      const right = str.slice(i);

      if (wordDict.includes(left) && canSplit(right)) {
        cache[str] = true;
        return true;
      }
    }

    cache[str] = false;
    return false;
  }

  return canSplit(s);
};
