var containsDuplicate = function (nums) {
  let set = new Set(); // create a set to keep track of items within the nums array
  for (const el of nums) set.add(el); // add items to the set, duplicates will automatically be ignored (set vs map)
  return set.size !== nums.length; // compare the length of nums array and the size of the set, which shows if there's a duplicate or not
};

// test cases
console.log(containsDuplicate([])); // false
console.log(containsDuplicate([1, 2, 3, 1])); // true
console.log(containsDuplicate([1, 2, 3, 4])); // false

// space - O(n) - creating a set to store elements
// time - O(n) - traverse through the array
