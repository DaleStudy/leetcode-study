function isPalindrome(s) {
  const letters = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  return letters === letters.split('').reverse().join('');
}
