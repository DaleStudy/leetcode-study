/*
Time Complexity : O(n^2)
Space Complexity : O(1)
*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int low = i + 1;
            int high = nums.length - 1;
            while (low < high) {
                int threeSum = nums[i] + nums[low] + nums[high];
                if (threeSum < 0) {
                    low = low + 1;
                } else if (threeSum > 0) {
                    high = high - 1;
                } else {
                    result.add(Arrays.asList(nums[i], nums[low], nums[high]));
                    while (low < high && nums[low] == nums[low + 1]) low++;
                    while (low < high && nums[high] == nums[high - 1]) high--;
                    low = low + 1;
                    high = high - 1;
                }
             }
        }

        return result;
    }
}
