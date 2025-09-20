function characterReplacement(s: string, k: number): number {
  let longestLength = 0;
  let windowStart = 0;

  const countMap = new Map<string, number>();
  let maxCount = 0;

  for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
    const currentCh = s[windowEnd];
    countMap.set(currentCh, (countMap.get(currentCh) || 0) + 1);

    maxCount = Math.max(maxCount, countMap.get(currentCh) || 0);
    if (windowEnd - windowStart + 1 - maxCount > k) {
      countMap.set(s[windowStart], (countMap.get(s[windowStart]) || 0) - 1);

      windowStart++;
    }
    longestLength = Math.max(longestLength, windowEnd - windowStart + 1);
  }

  return longestLength;
}
