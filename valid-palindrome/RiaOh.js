/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const arr = [...s];
  let text = "";
  for (let i = 0; i < arr.length; i++) {
    if (isAlphabet(arr[i]) === true && arr[i] !== " ") {
      text = text + arr[i].toLowerCase();
    } else if (isNumeric(arr[i]) === true && arr[i] !== " ") {
      text = text + arr[i];
    }
  }
  console.log("text -->", text);
  for (let i = 0; i < text.length / 2; i++) {
    if (text[i] !== text[text.length - 1 - i]) {
      return false;
    }
  }
  return true;
};

function isAlphabet(char) {
  return /[a-zA-Z]/.test(char);
}

function isNumeric(str) {
  return !isNaN(str);
}
