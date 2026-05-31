public class Geegong {

    /**
     * greedy algorithms 사용
     *
     * time complexity : O(N)
     * space complexity : O(N)
     * @param nums
     * @return
     */
    public boolean canJump(int[] nums) {
        // greedy algorithm
        int farthest = 0;
        int lastIdx = nums.length - 1;
        for (int idx=0; idx<nums.length; idx++) {
            // idx가 가장 멀리갈 수 있는 거리보다도 넘었다면 가망이 없는것
            if (idx > farthest) return false;
            int currentFarthest = idx + nums[idx];
            farthest = Math.max(farthest, currentFarthest);

            if (farthest >= lastIdx) return true;
        }

        return true;
    }


    // 아래 방법으로 풀면 TLE 발생
//    public boolean canJump(int[] nums) {
//        return recursion(0, nums);
//    }
//
//    public boolean recursion(int idx, int[] nums) {
//        int totalLength = nums.length;
//        if (idx == totalLength - 1) {
//            return true;
//        }
//
//        if (idx >= totalLength) {
//            return false;
//        }
//
//        int currVal = nums[idx];
//        while(currVal > 0) {
//            boolean result = recursion(idx + currVal, nums);
//            if (result) {
//                return true;
//            }
//
//            currVal--;
//        }
//
//        return false;
//    }

}
