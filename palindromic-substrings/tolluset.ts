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
    // If i is within the rightmost center, copy the pit value from the mirror
    if (i < right) {
      pit[i] = Math.min(right - i, pit[center * 2 - i]);
    }

    // Expand around i until it's not a palindrome and not over left or right
    while (
      i + pit[i] + 1 < len &&
      i - pit[i] - 1 >= 0 &&
      str[i + pit[i] + 1] === str[i - pit[i] - 1]
    ) {
      pit[i]++;
    }

    // If pit value is the new rightmost center, update center and right
    if (i + pit[i] > right) {
      center = i;
      right = i + pit[i];
    }

    // Add the number of palindromes with center i to the result
    result += Math.floor((pit[i] + 1) / 2);
  }

  return result;
}
