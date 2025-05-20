// TC: O(n)
// SC: O(1)
function characterReplacement(s: string, k: number): number {
  const freqMap = new Map<string, number>();
  let left = 0;
  let maxFreqCnt = 0;
  let result = 0;

  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    freqMap.set(ch, (freqMap.get(ch)! | 0) + 1);
    maxFreqCnt = Math.max(maxFreqCnt, freqMap.get(ch)!);

    while (right - left + 1 - maxFreqCnt > k) {
      // Shrink the sliding window by moving the left pointer to the right.
      // As we move left, decrease the frequency count of the character being excluded from the window.
      const ch = s[left];
      freqMap.set(ch, freqMap.get(ch)! - 1);
      left++;
    }

    result = Math.max(result, right - left + 1);
  }

  return result;
}

