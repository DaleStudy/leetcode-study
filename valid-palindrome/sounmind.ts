function isPalindrome(s: string): boolean {
  const filteredString = s.replace(/[^a-zA-Z0-9]/g, "").toUpperCase();

  let [left, right] = [0, filteredString.length - 1];

  while (left <= right) {
    if (filteredString[left] !== filteredString[right]) {
      return false;
    }

    left += 1;
    right -= 1;
  }

  return true;
}
