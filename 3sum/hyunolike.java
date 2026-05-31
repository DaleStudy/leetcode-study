class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        int n = nums.length;
        if (n < 3) return result;

        Arrays.sort(nums);

        for(int i = 0; i < n - 2; i++) {
            if(i > 0 && nums[i] == nums[i-1]) continue;

            int left = i + 1;
            int right = n - 1;

            while(left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if(sum < 0){
                    left++;
                }
                else if(sum > 0) {
                    right --;
                }
                else {
                                       // sum == 0 → 조합 하나 찾음
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // left, right 중복값 스킵
                    int leftVal = nums[left];
                    int rightVal = nums[right];

                    while (left < right && nums[left] == leftVal) left++;
                    while (left < right && nums[right] == rightVal) right--;
                }
            }
        }

        return result;
    }
}
