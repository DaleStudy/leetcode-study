const containsDuplicate = function (nums) {
  const data = new Set(nums);
  return data.size !== nums.length;
};
