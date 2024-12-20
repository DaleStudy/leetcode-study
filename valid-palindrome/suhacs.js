function isValidPalindrome(text) {
  let refinedTxt = text
    .replaceAll(/[^a-zA-Z0-9]/g, "")
    .replaceAll(" ", "")
    .toLowerCase();
  console.log(refinedTxt === [...refinedTxt].reverse().join("") ? true : false);
  return refinedTxt === [...refinedTxt].reverse().join("") ? true : false;
}

isValidPalindrome("A man, a plan, a canal: Panama"); //true
isValidPalindrome("race a car"); //false
isValidPalindrome(" "); //true
