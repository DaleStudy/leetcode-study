/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const newArr = [...s];
  if (newArr[0] === ")" || newArr[0] === "}" || newArr[0] === "]") {
    return false;
  }

  for (let i = 1; i < newArr.length; i++) {
    if (newArr[i] === ")" && newArr[i - 1] === "(") {
      newArr.splice(i - 1, 2);
      i = i - 2;
    }

    if (newArr[i] === "}" && newArr[i - 1] === "{") {
      newArr.splice(i - 1, 2);
      i = i - 2;
    }

    if (newArr[i] === "]" && newArr[i - 1] === "[") {
      newArr.splice(i - 1, 2);
      i = i - 2;
    }
  }
  return newArr.length === 0 ? true : false;
};
