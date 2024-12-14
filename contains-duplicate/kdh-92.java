class Solution {
    public boolean containsDuplicate(int[] nums) {
        /**
         * Constraints
         * - 1 <= nums[] <= 10^5
         * - -10^9 <= nums[i] <= 10^9
         *
         * Output
         * - true : 중복 값 존재
         * - false : 모든 값이 유일
         */

        // 해결법 1 (HashMap 방식 - HashSet 유사)
        // 시간복잡도: O(N), 공간 복잡도 : O(N)
        Map<Integer, Integer> countMap = new HashMap<>();

         for (int num: nums) {
             int count = countMap.getOrDefault(num, 0) + 1;
             if (count > 1) return true;
             countMap.put(num, count);
         }

         return false;

        // 해결법 2 (정렬)
        // 시간 복잡도 : O(N log N), 공간 복잡도 : O(1)
         Arrays.sort(nums);

         for (int i = 0; i < nums.length - 1; i++) {
             if (nums[i] == nums[i + 1]) return true;
         }

         return false;
    }
}
