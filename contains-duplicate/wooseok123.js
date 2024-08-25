// TC : O(n) | SC : O(n)

function containsDuplicate(nums) {
  let original_length = nums.length;
  let modified_length = new Set(nums).size;
  return original_length !== modified_length;
}
