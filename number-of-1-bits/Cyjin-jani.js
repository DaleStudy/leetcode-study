// tc: O(logn)
// sc: O(logn)
const hammingWeight_simple = function (n) {
  const binaryStr = n.toString(2);
  let answer = 0;

  for (char of binaryStr) {
    if (+char === 1) {
      answer++;
    }
  }

  return answer;
};

// toString(2)를 쓰지 않고 처리
// tc: O(logn)
// sc: O(1)
const hammingWeight = function (n) {
  let answer = 0;

  while (n >= 0) {
    const remains = n % 2;
    if (remains === 1) answer++;
    n = Math.floor(n / 2);
  }

  return answer;
};
