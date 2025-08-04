function isPalindrome(s: string): boolean {
  const converted = s.toLowerCase().replace(/[^a-z\d]/g, "");

  let l = 0;
  let r = converted.length - 1;

  while (l < r) {
    if (converted[l] !== converted[r]) return false;
    l++;
    r--;
  }

  return true;
}
