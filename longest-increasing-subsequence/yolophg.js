// Time Complexity: O(n log n)
// Space Complexity: O(n)

var lengthOfLIS = function (nums) {
  // array to store the smallest tail of all increasing subsequences of various lengths
  let subsequence = [];

  for (let num of nums) {
    // iterate through each number in the input array
    let left = 0,
      right = subsequence.length;

    // use binary search to find the position of the current number in the subsequence array
    while (left < right) {
      // calculate the middle index
      let mid = Math.floor((left + right) / 2);
      if (subsequence[mid] < num) {
        // move the left boundary to the right
        left = mid + 1;
      } else {
        // move the right boundary to the left
        right = mid;
      }
    }

    // if left is equal to the length of subsequence, it means num is greater than any element in subsequence
    if (left === subsequence.length) {
      // append num to the end of the subsequence array
      subsequence.push(num);
    } else {
      // replace the element at the found position with num
      subsequence[left] = num;
    }
  }

  // the length of the subsequence array is the length of the longest increasing subsequence
  return subsequence.length;
};
