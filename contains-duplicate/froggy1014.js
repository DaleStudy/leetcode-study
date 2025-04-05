// Set을 사용한 중복값 제거 후 길이 비교
function containsDuplicate(nums) {
  const numSet = new Set(nums);
  return numSet.size !== nums.length;
}

console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true
