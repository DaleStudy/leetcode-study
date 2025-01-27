// Time complexity: O(logn)
// Space complexity: O(1)

function hammingWeight(n) {
  let answer = 1;
  let current = n;

  while (current > 1) {
    if (current % 2 !== 0) {
      answer++;
    }

    current = Math.floor(current / 2);
  }

  return answer;
}
