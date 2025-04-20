// O(n) time, O(1) space

function isPalindrome(s: string): boolean {
  let low = 0,
    high = s.length - 1;

  while (low < high) {
    while (low < high && !s[low].match(/[0-9a-zA-Z]/)) {
      low++;
    }
    while (low < high && !s[high].match(/[0-9a-zA-Z]/)) {
      high--;
    }
    if (s[low].toLowerCase() !== s[high].toLowerCase()) {
      return false;
    }
    low++;
    high--;
  }
  return true;
}
