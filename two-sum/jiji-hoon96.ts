function twoSum(nums: number[], target: number): number[] {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j <= nums.length - 1; j++) {
      if (nums[i] + nums[j] === target) {
        console.log(i, j);
        return [i, j];
      }
    }
  }
}

twoSum([2, 7, 11, 15], 9); // [0,1]
twoSum([3, 2, 4], 6); // [1,2]
twoSum([3, 3], 6); // [0,1]
twoSum([3, 2, 3], 6); // [0,2]
