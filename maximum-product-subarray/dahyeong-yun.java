/**
 * TC : O(n)
 *   - nums 배열의 길이만큼 순회하므로 O(n)
 * SC : O(1)
 *   - int 변수만 사용하고 있으므로 O(1)
 */
class Solution {
    public int maxProduct(int[] nums) {
        int len = nums.length;
        if(len == 1) return nums[0];
        
        int answer = nums[0];
        int max = nums[0];
        int min = nums[0];
        
        for(int i = 1; i < len; i++) {
            int current = nums[i];
            int productFromMax = max * nums[i];
            int productFromMin = min * nums[i];

            max = Math.max(Math.max(current, productFromMax), productFromMin);
            min = Math.min(Math.min(current, productFromMax), productFromMin);

            answer = Math.max(max, answer);
        }
        
        return answer;
    }
}
