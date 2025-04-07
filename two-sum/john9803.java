class john9803 {
    public int[] twoSum(int[] nums, int target) {
        int[] result = n2Solve(nums, target);
        return result;
    }

    public int[] n2Solve(int[] nums, int target){
        // 일반적인 N^2 풀이
        int alpha_target = 0;
        int beta_target = 0;

        int[] truth_arr = new int[2];

        gnd: for(int i =0; i<nums.length; i++){
            alpha_target = nums[i];
            for( int j=i+1; j<nums.length; j++){
                beta_target = nums[j];
                if(alpha_target+beta_target==target){
                    truth_arr[0] = i;
                    truth_arr[1] = j;
                    break gnd;
                }
            }
        }
        return truth_arr;
    }

    // n2미만으로도 풀이해보기
    // public int[] 2nSolve(int[] nums, int target){
    // return [];
    // }
}\n