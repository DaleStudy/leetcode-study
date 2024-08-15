/*
 * TC: O(n)
 * SC: O(n)
 * */
function countSubstrings(s: string): number {
  const str = "#" + s.split("").join("#") + "#";
  const len = str.length;
  const pit = new Array(len).fill(0);
  let center = 0,
    right = 0,
    result = 0;

  for (let i = 0; i < len; i++) {
    // Set pit[i]
    if (i < right) {
      pit[i] = Math.min(right - i, pit[center * 2 - i]);
    }

    // Expand around i
    while (
      i + pit[i] + 1 < len &&
      i - pit[i] - 1 >= 0 &&
      str[i + pit[i] + 1] === str[i - pit[i] - 1]
    ) {
      pit[i]++;
    }

    // Update center and right
    if (i + pit[i] > right) {
      center = i;
      right = i + pit[i];
    }

    // Add to result
    result += Math.floor((pit[i] + 1) / 2);
  }

  return result;
}
