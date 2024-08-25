const encode = function (arr) {
  const encodedStr = arr.reduce((acc, cur) => acc + "#" + cur);
  return encodedStr;
};

const decode = function (str) {
  const decodedArr = str.split("#");
  return decodedArr;
};
