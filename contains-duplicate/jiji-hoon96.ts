function containsDuplicate(nums: number[]): boolean {
  let result = false;
  if (nums.length !== new Set(nums).size) result = true;

  return result;
}

containsDuplicate([1, 2, 3, 1]); //true
containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]); //true
