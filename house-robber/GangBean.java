class Solution {
    public int rob(int[] nums) {
        /**
            r[0] = a[0]
            r[1] = max(a[1], r[0])
            r[2] = max(r[1], a[2] + r[0])
            r[3] = max(r[2], a[3] + r[1])
            ...
            r[k] = max(r[k-1], a[k] + r[k-2]) O(1)
        */
        int[] r = new int[nums.length];

        for (int i = 0; i < nums.length; i++) { // O(N)
            if (i == 0) {
                r[i] = nums[i];
                continue;
            }
            if (i == 1) {
                r[i] = Math.max(nums[i], r[i-1]);
                continue;
            }
            r[i] = Math.max(r[i-1], nums[i] + r[i-2]);
        }

        return r[nums.length - 1];
    }
}

