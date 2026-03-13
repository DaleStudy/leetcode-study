const containsDuplicate = (nums) => {
  const uniqueCount = new Set(nums).size;
  return uniqueCount !== nums.length;
};
