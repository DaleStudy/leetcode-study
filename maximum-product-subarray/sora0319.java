public class sora0319 {
    public class Solution {
        public int maxProduct(int[] nums) {
            int result = nums[0];
            int max = 1;
            int min = 1;

            for (int num : nums) {
                int tempMax = Math.max(Math.max(max * num, min * num), num);
                int tempMin = Math.min(Math.min(max * num, min * num), num);

                max = tempMax;
                min = tempMin;

                result = Math.max(result, max);
            }

            return result;
        }
    }

}

