import java.util.*;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        /**
         runtime : 33ms
         memory : 51.15mb
         */

        // [idea] (1)정렬 (2)기준 인덱스를 하나 잡고 그 이후에 등장하는 수들에 대해서 two pointer 수행
        // (중요) **연속된 수들의 중복**이 있는지 체크하는 로직 필요!
        //     -> 정렬된 배열에서는 같은 숫자가 연속되어있으면 중복된 조합(=경우의 수)이 발생함
        //     -> 정렬된 배열의 앞 뒤 숫자들을 비교하며, 다음 수가 중복이 아닐때까지 넘기는 과정 필요

        // [time-complexity] : O(N^2)
        // [space-complexity] : O(K)(k=결과 조합의 개수)

        // 1.sort
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) { // start 인덱스가 (i+1)이므로 lenght-2까지만 순회

            // *중복 경우의 수 체크*
            if (i > 0 && nums[i] == nums[i-1]) continue;

            // 2.two pointer
            int start = i + 1;
            int end = nums.length - 1;

            while (start < end) {

                int sum = nums[i] + nums[start] + nums[end];

                if (sum == 0) {

                    result.add(List.of(nums[i], nums[start], nums[end]));

                    // // --------------- *중복 경우의 수 체크* ---------------
                    while (start < end && nums[start] == nums[start + 1]) {
                        start++;
                    }
                    while (end > start && nums[end] == nums[end - 1]) {
                        end--;
                    }
                    // ----------------------------------------------------

                    // 정답 찾았으므로(sum==0), 포인터 이동하여 다음 경우 탐색
                    start++;
                    end--;

                }
                else if (sum < 0) {
                    start++;
                }
                else if (sum > 0) {
                    end--;
                }

            }
        }

        return result;

    }
}
