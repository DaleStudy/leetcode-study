//time-complexity : O(n)
//space-complexity : O(n)

const maxProduct = function (nums) {
  let subarrays = [];
  let subarray = [];
  let zeroCount = 0;

  /* -------------------------------------------------------------------------- */
  /*                     nonzero subarray 잘라서 subarrays에 넣기                  */
  /* -------------------------------------------------------------------------- */
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      if (subarray.length > 0) {
        subarrays.push([...subarray]);
        subarray.length = 0; //각 element의 metadata를 garbage collection에 들어가야 하는 것으로 marking할 뿐이므로 O(1)!
      }
      zeroCount++;
      continue;
    }
    subarray.push(nums[i]);
  }
  if (subarray.length > 0) {
    subarrays.push([...subarray]);
  }

  /* -------------------------------------------------------------------------- */
  /*                   각 subarray의 maxProduct들 중 최대값 리턴하기                  */
  /* -------------------------------------------------------------------------- */
  if (zeroCount === 0) {
    return maxProductNonzero(nums);
  } else {
    let max = 0;
    for (let i = 0; i < subarrays.length; i++) {
      max = Math.max(maxProductNonzero(subarrays[i]), max);
    }
    return max;
  }
};

const maxProductNonzero = function (nonZeroNums) {
  if (nonZeroNums.length === 1) return nonZeroNums[0]; //firstNegativeIndex = lastNegativeIndex = 0이 되어 버려서 frontProduct와 backProduct 중 어느 것도 계산이 안 돼버리므로 early return으로 처리.

  let firstNegativeIndex = -1;
  let lastNegativeIndex = -1;
  let negativeCount = 0;
  for (let i = 0; i < nonZeroNums.length; i++) {
    if (nonZeroNums[i] < 0 && firstNegativeIndex !== lastNegativeIndex) {
      lastNegativeIndex = i;
      negativeCount++;
    }
    if (nonZeroNums[i] < 0 && firstNegativeIndex === lastNegativeIndex) {
      firstNegativeIndex = i;
      negativeCount++;
    }
  }

  if (negativeCount === 1) {
    lastNegativeIndex = firstNegativeIndex;
  }

  if (negativeCount % 2 === 0) {
    /* -------------------------------------------------------------------------- */
    /*                     음수 개수가 짝수 개면 그냥 전체 곱한 게 최대값임                  */
    /* -------------------------------------------------------------------------- */
    let product = 1;
    for (let i = 0; i < nonZeroNums.length; i++) {
      product *= nonZeroNums[i];
    }
    return product;
  } else {
    /* -------------------------------------------------------------------------- */
    /*        음수 개수가 홀수 개면 처음부터 lastNegativeIndex 직전까지 곱한 수 혹은          */
    /*        firstNegativeIndex부터 끝까지 곱한 수 중 하나가 최대값임                     */
    /* -------------------------------------------------------------------------- */
    let frontProduct = 1;
    let backProduct = 1;
    for (let i = 0; i < nonZeroNums.length; i++) {
      if (i < lastNegativeIndex) frontProduct *= nonZeroNums[i];
      if (i > firstNegativeIndex) backProduct *= nonZeroNums[i];
    }
    return Math.max(frontProduct, backProduct);
  }
};
