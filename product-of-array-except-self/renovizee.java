

// tag renovizee 2week
// https://github.com/DaleStudy/leetcode-study/issues/239
// https://leetcode.com/problems/product-of-array-except-self/  #238 #Medium
class Solution {
    // Solv1 :
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
    public int[] productExceptSelf(int[] nums) {

        boolean isZero = false;
        int zeroIndex = 0;

        int productExceptZero = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                if (isZero) { // zero가 2개면 모든 원소가 0임.
                    return new int[nums.length];
                }
                zeroIndex = i;
                isZero = true;
            } else {
                productExceptZero *= nums[i];
            }
        }

        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (isZero) {
                if (i != zeroIndex) {
                    result[i] = 0;
                } else {
                    result[i] = productExceptZero;
                }
            } else {
                result[i] = productExceptZero / nums[i];
            }

        }
        return result;
    }

}

//-------------------------------------------------------------------------------------------------------------
// Java 문법 피드백
//
//-------------------------------------------------------------------------------------------------------------
