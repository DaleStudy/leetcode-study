function containsDuplicate(nums) {
  const setLength = [...new Set(nums)].length;
  const numLength = nums.length;
  return numLength === setLength ? false : true;
}
//New function after feedback

function containDuplicate2(nums) {
  return nums.length !== new Set(nums).size;
}
