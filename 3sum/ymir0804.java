import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        int sum = 0;

        for (int i = 0; i < nums.length-2; i++) {
            int left = i + 1;
            int right = nums.length -1;
            if(i > 0 && nums[i-1] == nums[i]) {
                continue;
            }
            while (left < right ) {
                sum = nums[i] + nums[left] + nums[right];
                if(sum > 0) {
                    right--;
                } else if(sum < 0 ) {
                    left++;
                } else {
                    answer.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    left++;
                    right--;
                }
            }

        }
        return answer;
    }
}
