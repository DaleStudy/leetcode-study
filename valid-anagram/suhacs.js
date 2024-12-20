function isValidAnagram(s, t) {
  let temp = t;
  for (char of s) {
    temp = temp.replace(char, "");
  }
  return temp === "";
}
