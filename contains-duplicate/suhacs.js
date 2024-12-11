function containsDuplicate(nums) {
  const setLength = [...new Set(nums)].length;
  const numLength = nums.length;

  if (numLength === setLength) return false;
  else return true;
}

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));

//
