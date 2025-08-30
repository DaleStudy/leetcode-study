class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int multi = nums[0];
        answer[0] = 1;

        for(int i = 1; i < nums.length; i++){
            answer[i] = multi;
            multi *= nums[i];
        }

        multi = nums[nums.length-1];
        for(int i = nums.length-2; i >= 0; i--){
            answer[i] *= multi;
            multi *= nums[i];
        }

        return answer;
    }
}


