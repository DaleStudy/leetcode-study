var rob = function (nums) {
  // dynamic programming
  let prev = 0,
    curr = 0;

  for (let num of nums) {
    let temp = curr;
    curr = Math.max(num + prev, curr);
    prev = temp;
  }

  return curr;
};

// TC: O(n)
// SC: O(1)
