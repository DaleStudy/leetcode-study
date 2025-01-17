import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);

    Set<List<Integer>> answer = new HashSet<>();

    for(int i = 0; i < nums.length - 2; i++) {
      int left = i + 1;
      int right = nums.length - 1;

      while(left < right) {
        int sum = nums[i] + nums[left] + nums[right];

        if(sum < 0) {
          left++;
        } else if(sum > 0) {
          right--;
        } else{
          answer.add(List.of(nums[i], nums[left], nums[right]));

          left++;
          right--;
        }
      }
    }

    return new ArrayList<>(answer);
  }
}
