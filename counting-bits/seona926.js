/**
 * @param {number} n
 * @return {number[]}
 */
let countBits = function (n) {
  let result = [];

  for (let i = 0; i <= n; i++) {
    let binaryString = i.toString(2);

    let count = 0;
    for (let item of binaryString) {
      if (item === "1") {
        count++;
      }
    }

    result.push(count);
  }

  return result;
};

/*
  1. 시간복잡도 : O(nlogn)
    - 이진수 변환, 이진수 중 1의 개수를 세는 루프의 시간 복잡도: O(log i)
    - 작업이 총 n번 일어남
  2. 공간복잡도 : O(n)
    - result 배열의 공간 복잡도가 O(n) 
*/
