/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = (s) => {
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  const flipped = cleaned.split("").reverse().join("");

  return cleaned === flipped;
};
