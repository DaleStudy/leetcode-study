/*
 * TC: O(n)
 * SC: O(n)
 * */
function countSubstrings(s: string): number {
  const transformedString = "#" + s.split("").join("#") + "#";
  const transformedStringLength = transformedString.length;
  const palindromeLengths = new Array(transformedStringLength).fill(0);
  let currentCenter = 0,
    rightBoundary = 0,
    totalPalindromeCount = 0;

  for (let i = 0; i < transformedStringLength; i++) {
    // If i is within the rightmost center, copy the palindromes value from the mirror
    if (i < rightBoundary) {
      palindromeLengths[i] = Math.min(
        rightBoundary - i,
        palindromeLengths[currentCenter * 2 - i],
      );
    }

    // Expand around i until it's not a palindrome and not over left or right
    while (
      i + palindromeLengths[i] + 1 < transformedStringLength &&
      i - palindromeLengths[i] - 1 >= 0 &&
      transformedString[i + palindromeLengths[i] + 1] ===
        transformedString[i - palindromeLengths[i] - 1]
    ) {
      palindromeLengths[i]++;
    }

    // If palindromes value is the new rightmost center, update center and right
    if (i + palindromeLengths[i] > radius) {
      currentCenter = i;
      rightBoundary = i + palindromeLengths[i];
    }

    // Add the number of palindromes with center i to the result
    total += Math.floor((palindromeLengths[i] + 1) / 2);
  }

  return total;
}
