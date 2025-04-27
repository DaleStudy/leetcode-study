function isPalindrome(s: string): boolean {
  const str = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, "");
  return str === str.split("").reverse().join("");
}
