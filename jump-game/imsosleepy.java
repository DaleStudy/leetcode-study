// 현재 위치에서 최대로 갈 수 있는 인덱스의 이력을 갱신하면서 최대 범위를 넘지 않았나를 계속 판별하면 됨
// 처음엔 DP인줄 알았는데 DP 배열 없이 그냥 풀림
class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;  
        
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;
            } 
            
            maxReach = Math.max(maxReach, i + nums[i]); 
            if (maxReach >= nums.length - 1) {
                return true;
            } 
        }
        
        return true;
    }
}
