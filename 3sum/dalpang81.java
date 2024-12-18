/*
* 시간복잡도 : O(N^2)
* 공간복잡도 : O(1)
* */
import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0)
                {
                    // 합이 0인 경우 결과에 추가
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // 중복된 값 건너뛰기
                    while (left < right && nums[left] == nums[left + 1])
                        left++;

                    while (left < right && nums[right] == nums[right - 1])
                        right--;

                    left++;
                    right--;
                }
                else if (sum < 0)
                    left++;
                 else
                    right--;

            }
        }
        return result;
    }
}
