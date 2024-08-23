/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {

  let result = [];

  for (let i = 0; i <= n; i++) {

    let binary = i.toString(2);
    let sum = 0;

    for (let char of binary) {
      sum += Number(char);
    }
    result.push(sum);
  }

  return result;

};


console.log(countBits(2));
console.log(countBits(5));

/*
시간 복잡도: O(n * log n)
공간 복잡도: O(n)
*/
