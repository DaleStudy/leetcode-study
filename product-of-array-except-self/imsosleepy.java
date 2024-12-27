class Solution {
    // 누적곱을 이용한 풀이 int 크기를 보장해줘서 int를 사용하면된다.
    // O(N)의 시간복잡도가 나온다.
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1; 
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] = result[i] * right;
            right *= nums[i];
        }

        return result;
    }
}
