class Solution {
    public int[] productExceptSelf(int[] nums) {

        /**
         runtime : 2ms
         memory : 55.44mb
         */

        // [idea 03] : extra space-complexity optimization
        //    prefixProduct -> result 배열과 공유
        //    suffixProduct -> 변수로 대체
        // [time-complexity] : O(N)
        // [space-complexity] : O(N)(=> extra space-complexity : O(1)) 

        int[] result = new int[nums.length];
        result[0] = 1;

        // 1. prefix product 계산하여 result 배열에 저장
        for (int i = 1; i < result.length; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // 2. suffix product 계산하여 바로 result 배열에 반영
        int suffix = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            result[i] = result[i] * suffix;
            suffix = nums[i] * suffix;
            /**
             (1) suffix = 1
             (2) suffix = 4
             (3) suffix = 12
             (4) suffix = 24
             */
        }

        return result;

        /**
         runtime : 2ms
         memory : 56.05mb
         */

        // [idea 02] : production of prefix product and suffix product
        //   prefixProduct - 인덱스 기준, 자기 자신을 제외한 '이전 값들의 곱' 계산 및 저장
        //   suffixProduct - 인덱스 기준, 자기 자신을 제외한 '이후 값들의 곱' 계산 및 저장
        //   prefixProduct와 suffixProduct의 각 인덱스 값을 곱하면, 결국 자기 자신을 제외한 값들의 곱이 계산됨
        // [time-complexity] : O(N)
        // [space-complexity] : O(N)

        int[] prefixProduct = new int[nums.length];
        int[] suffixProduct = new int[nums.length];
        int[] result = new int[nums.length];

        prefixProduct[0] = 1;
        suffixProduct[suffixProduct.length - 1] = 1;

        for (int i = 1; i < prefixProduct.length; i++) {
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1];
        }

        for (int i = suffixProduct.length - 2; i >=0 ; i--) {
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < prefixProduct.length; i++) {
            result[i] = prefixProduct[i] * suffixProduct[i];
        }

        return result;

        /**
         "Time Limit Exeeded"
         */

        // [idea 01] : Brute Force
        // [time complexity] : O(N^2)
        // [space complexity] : O(N)

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int value = 1;
            for (int j = 0; j < nums.length; j++) {
                if (i == j) continue;
                value *= nums[j];
            }
            result[i] = value;
        }
        return result;

    }
}
