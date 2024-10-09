/**
 * https://leetcode.com/problems/minimum-window-substring
 * T.C. O(s + t)
 * S.C. O(t)
 */
function minWindow(s: string, t: string): string {
  let minLow = 0;
  let minHigh = s.length;

  const counts: Record<string, number> = {};
  for (const c of t) {
    counts[c] = (counts[c] || 0) + 1;
  }

  let included = 0;

  let low = 0;
  for (let high = 0; high < s.length; high++) {
    if (counts[s[high]]) {
      if (counts[s[high]] > 0) {
        included++;
      }
      counts[s[high]]--;
    }

    while (included === t.length) {
      if (high - low < minHigh - minLow) {
        minLow = low;
        minHigh = high;
      }

      if (counts[s[low]]) {
        counts[s[low]]++;
        if (counts[s[low]] > 0) {
          included--;
        }
      }

      low++;
    }
  }

  return minHigh === s.length ? '' : s.substring(minLow, minHigh + 1);
}
