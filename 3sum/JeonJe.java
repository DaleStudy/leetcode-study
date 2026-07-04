import java.util.*;

// TC: O(n^2)
// SC: O(1)
class Solution {

    public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> answer = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);

        for (int x = 0; x < n - 2; x++) {
            if (x > 0 && nums[x] == nums[x - 1]) continue;

            int left = x + 1;
            int right = n - 1;

            while (left < right) {
                if (nums[left] + nums[right] + nums[x] == 0) {
                    answer.add(Arrays.asList(nums[x], nums[left], nums[right]));

                    while (left + 1 < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right - 1 && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (nums[left] + nums[right] + nums[x] < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return answer;
    }
}
