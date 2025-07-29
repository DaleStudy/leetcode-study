import java.util.Arrays;

public class Geegong {

    /**
     * Time complexity : O(n)
     * Space complexity : O(1) (except result)
     *
     * 풀이 : prefix array , suffix array 를 각 배열마다 구하여 각 array에 해당되는 인덱스의 값들을 곱하여 결과값을 도출
     *
     * @param nums
     * @return
     */
    public int[] productExceptSelf(int[] nums) {

        int[] result = new int[nums.length];

        // 1. result 는 먼저 prefix 배열들의 곱으로 채운다.
        // ( prefix 배열이란 해당되는 index 이전의 배열요소값들을 의미)

        // 앞에서부터 누적되는 총 곱의 값
        int accumulatedProduct = 1;
        for (int index=0; index<nums.length; index++) {
            if (index == 0) {
                result[index] = 1;
                continue;
            }

            result[index] = accumulatedProduct * nums[index - 1];
            accumulatedProduct = result[index];
        }

        // 2. 배열의 뒤에서부터 product of suffix 값은 result 배열 하나하나에 대체한다.

        // nums 배열 안에서 뒤에서부터 누적되는 총 곱의 값
        accumulatedProduct = 1;
        for (int index=nums.length - 1; index >= 0; index--) {
            if (index == nums.length - 1) {
                accumulatedProduct = nums[index];
                continue;
            }

            result[index] = result[index] * accumulatedProduct;
            accumulatedProduct = accumulatedProduct * nums[index];
        }

        return result;
    }

}
