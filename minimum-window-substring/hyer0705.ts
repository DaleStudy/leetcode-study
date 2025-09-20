function minWindow(s: string, t: string): string {
  const m = s.length;
  const n = t.length;

  if (m < n) return "";

  let windowStart = 0;
  let minLen = Infinity;
  let substring = "";

  let requiredChar = n;

  const countCharMap = new Map<string, number>();
  for (const ch of t) {
    countCharMap.set(ch, (countCharMap.get(ch) || 0) + 1);
  }

  for (let windowEnd = 0; windowEnd < m; windowEnd++) {
    const endChar = s[windowEnd];

    if (countCharMap.has(endChar)) {
      if (countCharMap.get(endChar)! > 0) requiredChar--;
      countCharMap.set(endChar, (countCharMap.get(endChar) || 0) - 1);
    }

    while (requiredChar === 0) {
      const currentLen = windowEnd - windowStart + 1;
      if (currentLen < minLen) {
        minLen = currentLen;
        substring = s.substring(windowStart, windowEnd + 1);
      }

      const startChar = s[windowStart];
      windowStart++;

      if (countCharMap.has(startChar)) {
        countCharMap.set(startChar, (countCharMap.get(startChar) || 0) + 1);
        if (countCharMap.get(startChar)! > 0) requiredChar++;
      }
    }
  }

  return substring;
}
