// dp인건 부분 배열 문제인걸 확인하고 바로 알아차림
// 그런데 음수일때를 고려못해서 한참헤멤. 2번째 예제가 음수가 있을 수 있음을 알려주는 거였따...
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int[] maxProd = new int[n];
        int[] minProd = new int[n];

        maxProd[0] = nums[0];
        minProd[0] = nums[0]; // 음수일 경우를 대비
        int result = nums[0];

        for (int i = 1; i < n; i++) {
            maxProd[i] = Math.max(nums[i], Math.max(nums[i] * maxProd[i - 1], nums[i] * minProd[i - 1]));
            minProd[i] = Math.min(nums[i], Math.min(nums[i] * maxProd[i - 1], nums[i] * minProd[i - 1]));

            result = Math.max(result, maxProd[i]); 
        }

        return result;
    }
}
