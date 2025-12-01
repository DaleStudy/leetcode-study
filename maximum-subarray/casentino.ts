function maxSubArray(nums: number[]): number {
  function subSums(arr: number[], left: number, right: number) {
    if (left === right) {
      return nums[left];
    }
    const middle = Math.floor((left + right) / 2);

    const leftMax = subSums(arr, left, middle);
    const rightMax = subSums(arr, middle + 1, right);
    let leftSum = 0;
    let leftMaxSum = Number.NEGATIVE_INFINITY;
    for (let i = middle; i >= left; i--) {
      leftSum += arr[i];
      if (leftMaxSum < leftSum) {
        leftMaxSum = leftSum;
      }
    }
    let rightSum = 0;
    let rightMaxSum = Number.NEGATIVE_INFINITY;
    for (let i = middle + 1; i <= right; i++) {
      rightSum += arr[i];
      if (rightMaxSum < rightSum) {
        rightMaxSum = rightSum;
      }
    }

    return Math.max(leftMaxSum + rightMaxSum, leftMax, rightMax);
  }
  return subSums(nums, 0, nums.length - 1);
}
