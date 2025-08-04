// TC: O(n)
// SC: O(1)
function rob(nums: number[]): number {
  if (nums.length === 1) return nums[0];

  const robHouse = (start: number, end: number) => {
    let prevSum = 0;
    let prevPrevSum = 0;

    for (let i = start; i <= end; i++) {
      const temp = Math.max(prevSum, prevPrevSum + nums[i]);
      prevPrevSum = prevSum;
      prevSum = temp;
    }

    return prevSum;
  };

  return Math.max(robHouse(0, nums.length - 2), robHouse(1, nums.length - 1));
}
