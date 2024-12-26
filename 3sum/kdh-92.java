/**
 * 특이사항
 * 문제를 제대로 이해 못해서 풀이를 보며 이해했다.
 * 핵심은 중복 처리와 문제를 찾았을 때 종료가 아니라 다음 항목을 찾는 부분인 것 같다.
 * (추후 복습 예정)
 */

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        // (1) ArrayList
        // 시간복잡도 : O(N^2), 공간복잡도 : O(N)
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int sumNum = nums[i] + nums[j] + nums[k];

                if (sumNum > 0) k--;
                else if (sumNum < 0) j++;
                else {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;

                    while (nums[j] == nums[j - 1] && j < k) j++;
                }
            }
        }

        return result;
    }
}
