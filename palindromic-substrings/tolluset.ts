/*
 * TC: O(n)
 * SC: O(n)
 * */
function countSubstrings(s: string): number {
  const str = "#" + s.split("").join("#") + "#";
  const len = str.length;
  const pal = new Array(len).fill(0);
  let center = 0,
    radius = 0,
    total = 0;

  for (let i = 0; i < len; i++) {
    // If i is within the rightmost center, copy the palindromes value from the mirror
    if (i < radius) {
      pal[i] = Math.min(radius - i, pal[center * 2 - i]);
    }

    // Expand around i until it's not a palindrome and not over left or right
    while (
      i + pal[i] + 1 < len &&
      i - pal[i] - 1 >= 0 &&
      str[i + pal[i] + 1] === str[i - pal[i] - 1]
    ) {
      pal[i]++;
    }

    // If palindromes value is the new rightmost center, update center and right
    if (i + pal[i] > radius) {
      center = i;
      radius = i + pal[i];
    }

    // Add the number of palindromes with center i to the result
    total += Math.floor((pal[i] + 1) / 2);
  }

  return total;
}
