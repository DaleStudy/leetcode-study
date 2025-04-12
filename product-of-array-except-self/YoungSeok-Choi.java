class Solution {
    // 시간복잡도: O(3n) -> O(n)
    public int[] productExceptSelf(int[] nums) {

        int zeroCount = 0;
        int[] result = new int[nums.length];
        int productExceptZero = 1;
        int zeroIdx = 0;

        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 0) {
                zeroCount++;
            }
        }

        // NOTE: 0이 두개 이상일 때,  모든 배열의 원소가 0;
        if(zeroCount >= 2) {
            return result;
        }

        // NOTE: 0이 1개일 때, 0인 index만을 제외하고 모두 곱
        if(zeroCount == 1) {
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] == 0) {
                    zeroIdx = i;
                    continue;
                }
                productExceptZero *= nums[i];
            }
            
            result[zeroIdx] = productExceptZero;
            return result;
        }

        // NOTE: 0이 없을 때 모든수를 곱한 뒤 idx를 나누기.
        for(int i = 0; i < nums.length; i++) {
            productExceptZero *= nums[i];
        }

        for(int i = 0; i < nums.length; i++) {
            int copy = productExceptZero;
            result[i] = copy / nums[i];
        }

        return result;
    }
}
