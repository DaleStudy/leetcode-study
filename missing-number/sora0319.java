class Solution {
    public int missingNumber(int[] nums) {
        int result = 0;
        int[] counts = new int[nums.length+1];

        for(int n : nums){
            counts[n] = 1;
        }

        for(int i = 0; i < counts.length; i++){
            if(counts[i] == 0){
                result = i;
                break;
            }
        }

        return result;
    }
}

