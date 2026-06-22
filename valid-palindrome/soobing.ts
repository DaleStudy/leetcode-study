function isPalindrome(s: string): boolean {
  const original = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  let left = 0;
  let right = original.length - 1;

  while(left < right) {
      if(original[left] !== original[right]) return false;
      left++;
      right--;
  }
  return true;
};
