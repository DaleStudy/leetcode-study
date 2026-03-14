import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    // TC: O(n^2)
    // SC: O(n^2)
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();

        // Sort the array to use two-pointer technique.
        Arrays.sort(nums);

        // Exclude the last two elements from the loop
        // since the two pointers are involved in the iteration.
        for (int i = 0; i < nums.length - 2; i++) {
            if (i - 1 >= 0 && nums[i] == nums[i - 1]) {
                // Skip if this number is the same as the previous one,
                // so that we can avoid duplicate triplets.
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    ArrayList<Integer> list = new ArrayList<>(
                            Arrays.asList(nums[i], nums[left], nums[right]));
                    answer.add(list);

                    // According to the problem, we need to avoid duplicate triplets.
                    // Therefore, this loop is needed.
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }

        }

        return answer;
    }
}
