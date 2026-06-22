class Solution {
    public int maxProduct(int[] nums) {
        /**
        1.problem: subarray 중에 가장 큰 product return
        2.constraints
        - num.length min = 1
        - value min = -10, max=10
        3.solutions
        - bruteforce, time: O(n^2), space: O(1)
        - min, max value 추적, time: O(n), space: O(1)
         */
        int n = nums.length;
        if (n == 1) return nums[0];

        // int maxValue = Integer.MIN_VALUE;
        //  for(int i = 0; i <  n; i++) {
        //     int curValue = 1;
        //     for(int j = i; j < n; j++) {
        //         curValue *= nums[j];
        //         maxValue = Math.max(maxValue, curValue);
        //     }
        //  }

        int max = nums[0];
        int min = nums[0];
        int res = nums[0];

        for(int i = 1; i < n; i++) {
            int cur = nums[i];
            //현재값이 음수이면 min, max swap
            if(cur < 0) {
                int tmp = min;
                min = max;
                max = tmp;
            }
            max = Math.max(cur, max * cur);
            min = Math.min(cur, min * cur);

            res = Math.max(max, res);
        }
        return res;
    }
}
