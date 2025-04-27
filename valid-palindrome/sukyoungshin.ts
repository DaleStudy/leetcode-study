const alphaNumSet = new Set([..."abcdefghijklmnopqrstuvwxyz0123456789"]);

function isPalindrome(s: string): boolean {
  let normalized = "";

  for (const characters of s) {
    const lower = characters.toLowerCase();
    if (alphaNumSet.has(lower)) {
      normalized += lower;
    }
  }

  let left = 0;
  let right = normalized.length - 1;
  while (left < right) {
    if (normalized[left] !== normalized[right]) {
      return false;
    }
    left++;
    right--;
  }

  return true;
}
