class Solution {
        public List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        int len = nums.length;

        for (int i = 0; i < len - 2; i++) {
            // 인접한 같은 수라면, 지나감 
            if (i > 0 && nums[i] == nums[i-1]) continue; 
            
            int L = i + 1, H = len - 1;

            while(L < H) {
                if (nums[L] + nums[H] + nums[i] > 0) {
                    H--;
                } else if (nums[L] + nums[H] + nums[i] < 0) {
                    L++;
                } else {
                    answer.add(Arrays.asList(nums[i],  nums[L], nums[H]));
                    // 중복을 제거
                    while (L < H && nums[L] == nums[L+1]) L++;
                    while (L < H && nums[H] == nums[H-1]) H--;
                    L++;
                    H--;
                }
            }
        }
        return answer;
    }
}
