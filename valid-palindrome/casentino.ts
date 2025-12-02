function isPalindrome(s: string): boolean {
  let start = 0;
  let last = s.length - 1;
  while (start < last) {
    while (start < last && !isAlphanumeric(s.charAt(start))) {
      start += 1;
    }
    while (start < last && !isAlphanumeric(s.charAt(last))) {
      last -= 1;
    }
    if (s.charAt(start).toLowerCase() !== s.charAt(last).toLowerCase()) {
      return false;
    }
    start += 1;
    last -= 1;
  }
  return true;
}

function isAlphanumeric(character: string) {
  const characterCode = character.charCodeAt(0);
  const lowerStart = "a".charCodeAt(0);
  const lowerEnd = "z".charCodeAt(0);
  const upperStart = "A".charCodeAt(0);
  const upperEnd = "Z".charCodeAt(0);
  const numericStart = "0".charCodeAt(0);
  const numericEnd = "9".charCodeAt(0);
  if (upperStart <= characterCode && upperEnd >= characterCode) {
    return true;
  }
  if (lowerStart <= characterCode && lowerEnd >= characterCode) {
    return true;
  }
  if (numericStart <= characterCode && numericEnd >= characterCode) {
    return true;
  }
  return false;
}
