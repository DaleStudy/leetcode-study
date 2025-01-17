function isPalindrome(s: string): boolean {
  const convertWord = s.toLowerCase().match(/[a-z0-9]/g) ?? [];
  const length = convertWord.length;
  for (let i = 0; i < length / 2; i++) {
    if (convertWord[i] !== convertWord[length - 1 - i]) {
      return false;
    }
  }

  return true;
}
