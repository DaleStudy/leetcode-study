function isPalindrome(s: string): boolean {
  // 1. filter out non-alphanumeric characters
  const validChars =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnlopqrstuvwxyz0123456789";

  // 2. compare the first and last characters
  let i = 0;
  let j = s.length - 1;

  while (i < j) {
    const head = s[i];
    const tail = s[j];

    if (!validChars.includes(head)) {
      // 3. if the characters are not alphanumeric, move the pointer inward
      i++;
    } else if (!validChars.includes(tail)) {
      // 3. if the characters are not alphanumeric, move the pointer inward
      j--;
    } else if (head.toLowerCase() !== tail.toLowerCase()) {
      // 4. if the characters are not the same, return false
      return false;
    } else {
      // 5. if the characters are the same, move the pointers inward
      i++;
      j--;
    }
  }
  return true;
}
