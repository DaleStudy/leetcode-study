import java.util.*;

class Solution {
    /* 시간 복잡도: O(N^2)
    * - for 루프: O(N)
    *   - while 루프: O(N) -> N^2
    * 공간 복잡도: O(K), answer의 K = List<Integer> 개수
    */ 
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    answer.add(List.of(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left += 1;
                    while (left < right && nums[right] == nums[right - 1]) right -= 1;
                    left += 1;
                    right -= 1;
                } else if (sum < 0) left += 1;
                else right -= 1;
            }
        }

        return answer;
    }
}
