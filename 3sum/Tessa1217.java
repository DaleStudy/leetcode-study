import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

// 정수 배열 nums가 주어질 때 nums[i], nums[j], nums[k]로 이루어진 배열을 반환하시오
// 반환 배열 조건: i 가 j와 같지 않고, i가 k와 같지 않으며 세 요소의 합이 0인 배열
class Solution {

    // 시간복잡도: O(n^2)
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);

        List<List<Integer>> answer = new ArrayList<>();

        int left = 0;
        int right = 0;
        int sum = 0;

        for (int i = 0; i < nums.length - 2 && nums[i] <= 0; i++) {

            // 중복 제거
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            left = i + 1;
            right = nums.length - 1;

            while (left < right) {

                sum = nums[i] + nums[left] + nums[right];
                // System.out.println(String.format("%d, %d, %d", i, left, right));
                // System.out.println(String.format("%d + %d + %d = %d", nums[i], nums[left], nums[right], sum));
                if (sum < 0) {
                    left++;
                    continue;
                }
                if (sum > 0) {
                    right--;
                    continue;
                }

                answer.add(List.of(nums[i], nums[left], nums[right]));

                // 중복 제거
                while (left < right && left + 1 < nums.length && nums[left] == nums[left + 1]) {
                    left++;
                }
                while (left < right && right - 1 >= 0 && nums[right] == nums[right - 1]) {
                    right--;
                }
                left++;
                right--;

            }
        }

        return answer;
    }

}

