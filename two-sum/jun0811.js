// Time Complexity : O(N^2)

var twoSum = function (nums, target) {
  const l = nums.length;
  for (let i = 0; i < l; i++) {
    for (let j = i + 1; j < l; j++) {
      const value = nums[i] + nums[j];
      if (value == target) return [i, j];
    }
  }
};

// Time Complexity : O(N)

var twoSum = function (nums, target) {
  const Map = {};

  nums.forEach((num, idx) => {
    Map[num] = idx;
  });

  for (const idx in nums) {
    const value = target - nums[idx];
    if (Map[value] >= 0 && Map[value] != idx) return [+idx, Map[value]];
  }
};
