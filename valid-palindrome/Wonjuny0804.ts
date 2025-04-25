function isPalindrome(s: string): boolean {
  const lowered = s.toLowerCase();
  const removed = lowered.replaceAll(
    /[!|\s|.\\|\|()@#$%^&*_\-+,:'"\[\]{}\?;`]/g,
    ""
  );

  for (let i = 0; i < removed.length; i++) {
    if (removed[i] !== removed[removed.length - i - 1]) return false;
  }
  return true;
}
