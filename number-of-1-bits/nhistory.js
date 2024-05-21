var hammingWeight = function (n) {
  let count = 0;
  while (n) {
    // Check rightmost bit is equal to 1 by using bitwise AND operator
    count += n & 1;
    // Remove rightmost bit from n by using right shift operator
    n >>= 1;
  }
  return count;
};

// TC: O(1) -> The worst case of 32-integer would be O(32)
// SC: O(1)
