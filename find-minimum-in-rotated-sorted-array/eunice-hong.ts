
/**
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
function findMin(nums: number[]): number {
    let index = 0;
    // find the index of where the value is greater than the next value
    while (nums[index] < nums[(index + 1) % nums.length]) {
      index++;
    }
    // return the next value
    return nums[(index + 1) % nums.length]
};