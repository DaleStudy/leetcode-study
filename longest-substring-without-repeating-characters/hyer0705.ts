function lengthOfLongestSubstring(s: string): number {
  let maxLen = 0;

  const used = new Set<string>();
  let windowStart = 0;

  for (let windowEnd = 0; windowEnd < s.length; windowEnd++) {
    const currentCh = s[windowEnd];
    while (used.has(currentCh)) {
      used.delete(s[windowStart]);
      windowStart++;
    }

    used.add(currentCh);
    maxLen = Math.max(maxLen, windowEnd - windowStart + 1);
  }

  return maxLen;
}
