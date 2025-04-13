/* [time-complexity]: O(n)
   [space-complexity]: O(1)
 */
public class JEONGBEOMKO {

    class Solution {
        public int[] productExceptSelf(int[] nums) {
            int n = nums.length;
            int[] result = new int[n];

            // 왼쪽 곱 계산
            result[0] = 1;
            for (int i = 1; i < n; i++) {
                result[i] = result[i - 1] * nums[i - 1];
            }

            // 오른쪽 곱과 동시에 결과 계산
            int rightProduct = 1;
            for (int i = n - 1; i >= 0; i--) {
                result[i] = result[i] * rightProduct;
                rightProduct *= nums[i];
            }

            return result;
        }
    }
}
