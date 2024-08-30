function productExceptSelf(nums: number[]): number[] {
  /* #Solution 1
   * sum: 전체 곱을 구한다.
   * zeroCount: 0의 개수가 몇개인지 센다.
   * 1. 자신이 0이면,
   * 1-1. 자신이외의 0이 있는지 확인하고 있으면 0을 return
   * 1-2. 자신 이외에 0이 없으면 전체 곱을 return
   * 2. 자신이 0이 아니면
   * 2-1. zeroCount가 있는지 보고 있으면 0을 return
   * 2-2. zero가 없으면 sum/self를 return
   */
  let zeroCount = 0;
  const sum = nums.reduce((p, c) => {
    if (c === 0) {
      zeroCount += 1;
      return p;
    }
    p = p * c;
    return p;
  }, 1);

  const hasZero = zeroCount > 0;

  if (zeroCount === nums.length) return Array(nums.length).fill(0);

  return nums.map((n) => {
    if (n === 0) {
      // 자신 이외에 0이 있을때
      if (zeroCount - 1 > 0) {
        return 0;
      }

      return sum;
    }

    if (hasZero) return 0;
    return sum / n;
  });
  // TC: O(N)
  // SC: O(N)

  /* #Solution 2
   * 1. prefix: 자신을 제외한 자기 인덱스 앞까지의 곱을 저장한다.
   * 2. suffix: 자신을 제외한 자기 뒤까지의 곱을 저장한다.
   * 3. answer[i] = prefix[i] * suffix[i]
   */
  //   const n = nums.length;

  //   const prefix = new Array(n).fill(1);
  //   const suffix = new Array(n).fill(1);

  //   for (let i = 1; i < n; i++) {
  //     prefix[i] = prefix[i - 1] * nums[i - 1];
  //   }

  //   for (let i = n - 2; i >= 0; i--) {
  //     suffix[i] = suffix[i + 1] * nums[i + 1];
  //   }

  //   const answer = [];
  //   for (let i = 0; i < n; i++) {
  //     answer[i] = prefix[i] * suffix[i];
  //   }

  //   return answer;
}
// TC: O(N)
// SC: O(N)
