/**
 정수 배열 nums가 주어질 때 answer[i]가 nums[i]를 제외한 나머지 요소의 곱인 answer 배열을 반환하시오.
 */
public class Solution {

    /** 시간복잡도 O(n) */
    public int[] productExceptSelf(int[] nums) {

        int[] answer = new int[nums.length];

        int start = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] = start;
            start *= nums[i];
        }

        int end = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= end;
            end *= nums[i];
        }

        return answer;
    }
}

