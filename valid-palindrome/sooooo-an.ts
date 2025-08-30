function isPalindrome(s: string): boolean {
  const cleanString = s
    .toLowerCase()
    .replace(/\s+/g, "")
    .replace(/[^a-z0-9]/g, "");

  let left = 0;
  let right = cleanString.length - 1;

  while (left < right) {
    if (cleanString[left] !== cleanString[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
}
