const twoSum = function (nums, target) {
  let memo = {};

  for (let i = 0; i < nums.length; i++) {
    let current = nums[i];
    let needed = target - current;

    if (needed in memo) {
      return [memo[needed], i];
    }

    memo[current] = i;
  }
};
