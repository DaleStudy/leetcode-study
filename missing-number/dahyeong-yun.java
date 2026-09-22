/**
 * TC : O(n)
 *   - 배열을 한 번 순회하면서 합을 구하기 때문에 n
 * SC : O(1)
 *  - 별도 유의미한 공간 할당이 없음
 */
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int total = n * (n + 1) / 2;
        int sum = 0;
        for(int num : nums) sum+=num;
        return total - sum;
    }
}
