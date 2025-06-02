class Solution {

    // 시간복잡도: O(n)
    public int maxProduct(int[] nums) {

        if (nums == null || nums.length == 0) {
            return 0;
        }

        // 최대 곱 케이스
        int maxProduct = nums[0];
        // 최소 곱 케이스
        int minProduct = nums[0];
        // 최대 값
        int max = nums[0];

        // DP로 풀이하였지만 음수 * 음수의 반례 케이스 발생하여 해당 풀이로 수정
        // Test Case : [-2, 3, -4] => dp로 풀이 시 3이 반환되는 문제 있었음

        for (int i = 1; i < nums.length; i++) {

            int current = nums[i];

            // 음수일 경우 : 최소 곱과 최대 곱 위치 바꿈
            if (current < 0) {
                int tempMax = maxProduct;
                maxProduct = Math.max(current, minProduct * current);
                minProduct = Math.min(current, tempMax * current);
            } else {
                maxProduct = Math.max(current, maxProduct * current);
                minProduct = Math.min(current, minProduct * current);
            }

            max = Math.max(max, maxProduct);

        }

        return max;

    }
}

