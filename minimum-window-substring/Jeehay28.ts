// TC: O(m+ n), where m is the length of s, and n is the length of t
// SC: O(n)

function minWindow(s: string, t: string): string {
  const tCnt = new Map<string, number>();
  const windowCnt = new Map<string, number>();

  for (const ch of t) {
    tCnt.set(ch, (tCnt.get(ch) || 0) + 1);
  }

  let left = 0;
  let validWindowKeySize = 0;
  let minStrLength = Infinity;
  let minLeft = 0;

  for (let right = 0; right < s.length; right++) {
    const ch = s[right];

    windowCnt.set(ch, (windowCnt.get(ch) || 0) + 1);

    if (tCnt.has(ch) && tCnt.get(ch) === windowCnt.get(ch)) {
      validWindowKeySize++;
    }

    // When windowCnt's keys include all the keys from tCnt
    while (tCnt.size === validWindowKeySize && left <= right) {
      // Update the minimum window details: start index (minLeft) and length (minStrLength)
      if (right - left + 1 < minStrLength) {
        minStrLength = right - left + 1;
        minLeft = left;
      }

      // shrink the window by moving the left pointer
      const ch = s[left];
      windowCnt.set(ch, windowCnt.get(ch)! - 1);

      if (tCnt.has(ch) && windowCnt.get(ch)! < tCnt.get(ch)!) {
        validWindowKeySize--;
      }

      left++;
    }
  }

  return minStrLength === Infinity
    ? ""
    : s.slice(minLeft, minLeft + minStrLength);
}
