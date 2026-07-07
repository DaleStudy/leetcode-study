import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        /*
         * 세 수의 합이 0이 되는 조합을 찾는다.
         *
         * nums[i]를 하나 고정하면,
         * 나머지 두 수를 찾는 Two Sum 문제로 바꿀 수 있다.
         *
         * seen에는 현재 i 기준으로 지나온 값들을 저장한다.
         * target이 seen에 있으면 nums[i] + target + nums[j] = 0 이다.
         *
         *
         * 시간 복잡도: O(n^2)
         * 공간 복잡도: O(n)
         */

        Arrays.sort(nums);

        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            // 같은 기준값은 한 번만 사용
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // 기준값이 양수면 합이 0이 될 수 없음
            if (nums[i] > 0) {
                break;
            }

            Set<Integer> seen = new HashSet<>();

            for (int j = i + 1; j < nums.length; j++) {
                int target = -nums[i] - nums[j];

                if (seen.contains(target)) {
                    answer.add(Arrays.asList(nums[i], target, nums[j]));

                    // 같은 nums[j]는 중복 조합을 만들 수 있으므로 스킵
                    while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
                        j++;
                    }
                }

                seen.add(nums[j]);
            }
        }

        return answer;
    }
}
