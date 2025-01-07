/*
시간 복잡도: O(n)
공간 복잡도: O(1)

1 ~ n의 합이 n * (n + 1) / 2 라는 점을 활용
*/
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int ans = n * (n + 1) / 2;
        for (int i = 0; i < n; i++) {
            ans -= nums[i];
        }
        return ans;
    }
}
