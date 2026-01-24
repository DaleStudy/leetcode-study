/*
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        long expected = n * (n + 1) / 2;
        long actual = 0;
        for (int x : nums) {
            actual += x;
        }
        return (int) (expected - actual);
    }
}

/*
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(1)
 */
class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i != nums[i]) {
                return i;
            }
        }
        return nums.length;
    }
}
