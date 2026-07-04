const containsDuplicate = (nums) => {
  const set = new Set(nums);
  return set.size !== nums.length;
};
