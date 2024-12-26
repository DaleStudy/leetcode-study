import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> set = new HashSet<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2; i++) {
            int start = i + 1;
            int end = nums.length - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if (sum < 0 ) {
                    start++;
                } else if (sum > 0) {
                    end--;
                }else {
                    set.add(Arrays.asList(nums[i], nums[start], nums[end]));
                    start++;
                    end--;
                }
            }
        }
        return set.stream().toList();
    }
}
