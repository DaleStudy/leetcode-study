let hammingWeight = function (n) {
  return DecToBinAndGetSetBits(n);
};

// TC : O(log n) | SC : O(1)

let DecToBinAndGetSetBits = (n) => {
  let targetNum = n;
  let result = 0;
  while (targetNum > 0) {
    let remainder = targetNum % 2;
    if (remainder === 1) result += 1;
    targetNum = parseInt(targetNum / 2);
  }
  return result;
};

// TC : O(log n) | SC : O(log n)
// 근데 사실 split 메서드 자체는 o(n)인데, toString과정을 통해 log(n)의 개수만큼 나와버린 것이면 o(log n)이라고 표기해도 되는걸까?

// let DecToBinAndGetSetBits = (n) => {
//     let target = n;
//     let bin = n.toString(2);
//     return bin.split("").filter((el) => el == 1).length
// }

// TC : O(log n) | SC : O(log n)

// let DecToBinAndGetSetBits = (n) => {
//     let target = n;
//     let bin = n.toString(2);
//     let matches = bin.match(/1/g);
//     return matches.length
// }
